# vintrick-backend/app/utils/vintrace_client.py

import os
import json
import requests

class VintraceSmartClient:
    BASE_URLS = {
        "v6": "https://us61.vintrace.net/smwe/api/v6",
        "v7": "https://us61.vintrace.net/smwe/api/v7",
    }

    def __init__(self, api_key=None, endpoint_map_path=None):
        self.api_key = api_key or os.getenv("VINTRACE_API_TOKEN")
        endpoint_map_path = endpoint_map_path or os.getenv("ENDPOINT_MAP_PATH")
        if not self.api_key:
            raise RuntimeError("VINTRACE_API_TOKEN must be set in .env or passed in.")
        if not endpoint_map_path or not os.path.exists(endpoint_map_path):
            raise RuntimeError(f"Endpoint map file not found: {endpoint_map_path}")
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