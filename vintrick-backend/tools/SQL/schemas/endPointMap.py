# builder.py

import yaml
import glob
import os
import re
import json
import subprocess

def generate_combined_models(yaml_folder, output_py_path):
    temp_files = []
    for yaml_file in glob.glob(os.path.join(yaml_folder, "*.yml")) + glob.glob(os.path.join(yaml_folder, "*.yaml")):
        temp_file = yaml_file + ".models.tmp.py"
        subprocess.run([
            "datamodel-codegen",
            "--input", yaml_file,
            "--output", temp_file,
            "--input-file-type", "openapi",
            "--use-standard-collections" 
        ], check=True)
        temp_files.append(temp_file)
        print(f"Generated models for {yaml_file}")

    os.makedirs(os.path.dirname(output_py_path), exist_ok=True)

    # Combine, handling __future__ imports correctly
    all_lines = []
    future_line = None
    for temp_file in temp_files:
        with open(temp_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("from __future__ import annotations"):
                    if not future_line:
                        future_line = line
                    # skip duplicates
                else:
                    all_lines.append(line)
        os.remove(temp_file)

    # Write combined file
    with open(output_py_path, "w", encoding="utf-8") as out_f:
        if future_line:
            out_f.write(future_line)
        out_f.writelines(all_lines)
    print(f"✅ Combined models written to {output_py_path}")

def patch_models_py_for_pydantic_v2(models_path):
    """Ensures generated models.py is v2-ready for Pydantic config."""
    if not os.path.exists(models_path):
        print(f"❌ Models file not found: {models_path}")
        return
    with open(models_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Remove any old Config class block for arbitrary_types_allowed
    code, _ = re.subn(
        r"\nclass Config:\n\s+arbitrary_types_allowed = True\n\nBaseModel\.model_config = Config\n",
        "\n",
        code,
        flags=re.MULTILINE,
    )

    # Insert v2 style patch after pydantic import(s)
    patch = "BaseModel.model_config = RootModel.model_config = {'arbitrary_types_allowed': True}\n"
    if patch not in code:
        lines = code.splitlines(keepends=True)
        insert_at = 0
        for i, l in enumerate(lines):
            if l.startswith("from pydantic"):
                insert_at = i + 1
        lines.insert(insert_at, patch)
        code = ''.join(lines)

    with open(models_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ Patched {models_path} for pydantic v2 config")

def infer_version_from_filename(filename):
    m = re.search(r'v(\d+)', filename)
    return f"v{m.group(1)}" if m else "unknown"

def clean_path_for_key(path):
    clean = re.sub(r"\{([^}]+)\}", r"<\1>", path)
    clean = clean.replace("//", "/").rstrip("/")
    return clean

def resolve_ref(ref, spec):
    if not ref.startswith("#/"):
        raise ValueError(f"Unsupported $ref: {ref}")
    parts = ref.lstrip("#/").split("/")
    obj = spec
    for part in parts:
        obj = obj.get(part)
        if obj is None:
            raise KeyError(f"Could not resolve $ref {ref}")
    return obj

def expand_parameters(param_list, spec):
    expanded = []
    for param in param_list:
        if "$ref" in param:
            try:
                resolved = resolve_ref(param["$ref"], spec)
                expanded.append(resolved)
            except Exception as e:
                print(f"⚠️ Failed to resolve {param['$ref']}: {e}")
        else:
            expanded.append(param)
    return expanded

def extract_schema_name(schema):
    if not schema:
        return None
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    for key in ["allOf", "oneOf", "anyOf"]:
        if key in schema and schema[key]:
            return extract_schema_name(schema[key][0])
    return None

def build_endpoint_map(yaml_folder, out_json_path):
    endpoint_map = {}
    for yaml_file in glob.glob(os.path.join(yaml_folder, "*.yaml")) + glob.glob(os.path.join(yaml_folder, "*.yml")):
        api_version = infer_version_from_filename(os.path.basename(yaml_file))
        with open(yaml_file, "r", encoding="utf-8") as f:
            try:
                spec = yaml.safe_load(f)
            except Exception as e:
                print(f"Could not parse {yaml_file}: {e}")
                continue
        for path, methods in spec.get("paths", {}).items():
            path_parameters = expand_parameters(methods.get("parameters", []), spec)
            for http_method, op in methods.items():
                if http_method.lower() == "parameters":
                    continue
                op_list = op if isinstance(op, list) else [op]
                for op_item in op_list:
                    if not isinstance(op_item, dict):
                        continue
                    desc = op_item.get("summary") or op_item.get("description", "")
                    op_parameters = expand_parameters(op_item.get("parameters", []), spec)
                    all_parameters = path_parameters + op_parameters
                    request_schema = None
                    if 'requestBody' in op_item:
                        content = op_item['requestBody'].get('content', {})
                        app_json = content.get('application/json', {})
                        schema = app_json.get('schema', {})
                        request_schema = extract_schema_name(schema)
                    response_schema = None
                    responses = op_item.get('responses', {})
                    resp_codes = [str(c) for c in responses if str(c).startswith("2")]
                    resp_codes = sorted(resp_codes, key=lambda x: int(re.sub(r"\D", "", x) or "999"))
                    for rc in resp_codes:
                        content = responses[rc].get('content', {})
                        app_json = content.get('application/json', {})
                        schema = app_json.get('schema', {})
                        response_schema = extract_schema_name(schema)
                        if response_schema:
                            break
                    path_for_key = clean_path_for_key(path)
                    key = f"{http_method.upper()}:{path_for_key}"
                    if key in endpoint_map:
                        print(f"⚠️ Duplicate key found: {key} (ignoring {api_version} {http_method} {path})")
                        continue
                    endpoint_map[key] = {
                        "version": api_version,
                        "http_method": http_method.upper(),
                        "path": path,
                        "description": desc,
                        "parameters": all_parameters,
                        "request_schema": request_schema,
                        "response_schema": response_schema
                    }
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(endpoint_map, f, indent=2)
    print(f"✅ Saved endpoint_map to {out_json_path}")

if __name__ == "__main__":
    generate_combined_models(
        r"DataMain/Vintrace_OpenAPI/",
        r"DataMain/Models/models.py"
    )
    patch_models_py_for_pydantic_v2(
        r"DataMain/Models/models.py"
    )
    build_endpoint_map(
        r"DataMain/Vintrace_OpenAPI/",
        r"DataMain/Models/endpoint_map.json"
    )
