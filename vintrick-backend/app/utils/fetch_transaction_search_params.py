# vintrick-backend/app/utils/fetch_transaction_search_params.py

import requests

def fetch_transaction_search_params(api_base_url="http://localhost:3000"):
    url = f"{api_base_url}/api/meta/transaction-search-params"
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    return data["params"]  # Array of param metadata