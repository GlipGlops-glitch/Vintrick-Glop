import requests
import json

class VintraceSmartClient:
    BASE_URLS = {
        "v6": "https://us61.vintrace.net/smwe/api/v6",
        "v7": "https://us61.vintrace.net/smwe/api/v7",
    }

    def __init__(self, api_key, endpoint_map_path):
        self.api_key = api_key
        with open(endpoint_map_path, "r", encoding="utf-8") as f:
            self.endpoint_map = json.load(f)

    def call_endpoint(self, key, params=None, data=None, headers=None):
        ep = self.endpoint_map.get(key)
        if not ep:
            raise ValueError(f"Endpoint '{key}' not found in map.")
        version = ep['version']
        url = f"{self.BASE_URLS[version]}{ep['path']}"
        method = ep['http_method'].lower()
        hdrs = headers or {}
        hdrs.update({
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        resp = requests.request(
            method=method,
            url=url,
            params=params,
            json=data,
            headers=hdrs,
        )
        resp.raise_for_status()
        return resp.json()

    def write_available_endpoints(self, out_path="C:/Users/casey/OneDrive/Desktop/code/Main/Models/Endpoints.txt", with_description=True):
        lines = ["Available endpoints:\n"]
        for key, ep in self.endpoint_map.items():
            line = f"- {ep['version']} | {ep['http_method']} | {key.split(':',1)[1]}"
            if with_description and ep.get("description"):
                line += f"  |  {ep.get('description','')}"
            lines.append(line)
        lines.append("\n(Use the key 'METHOD:/resource/path' with call_endpoint(key))")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"✅ Wrote endpoints to {out_path}")

    def get_parameters_for_key(self, key):
        """
        Returns a list of parameters (as defined in OpenAPI) for a given endpoint key.
        """
        ep = self.endpoint_map.get(key)
        if not ep:
            raise ValueError(f"Endpoint '{key}' not found in map.")
        params = ep.get("parameters", [])
        if not params:
            print(f"No parameters defined for {key}")
            return []
        print(f"Parameters for {key}:")
        for p in params:
            print(f"  - name: {p.get('name')}, in: {p.get('in')}, required: {p.get('required', False)}, type: {p.get('schema',{}).get('type')}")
        return params

# Example usage:
if __name__ == "__main__":
    client = VintraceSmartClient(
        api_key="YOUR_API_KEY",
        endpoint_map_path=r"C:/Users/casey/OneDrive/Desktop/code/Main/Models/endpoint_map.json"
    )

    client.write_available_endpoints(out_path="C:/Users/casey/OneDrive/Desktop/code/Main/Models/Endpoints.txt")

    # Example: Get parameters for a specific endpoint
    client.get_parameters_for_key("GET:/party/list")
    # To call an endpoint:
    # result = client.call_endpoint("GET:/vessel-details-report", params={"param1": "value"}, data=None)
    # print(result)
