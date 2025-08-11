# vintrick-backend/app/vintrace_api.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_VINTRACE_URL = os.getenv("BASE_VINTRACE_URL", "https://us61.vintrace.net")
ENDPOINT = os.getenv("ENDPOINT", "smwe/api/v6/transaction/search/")
VINTRACE_API_TOKEN = os.getenv("VINTRACE_API_TOKEN")

def get_vintrace_transaction_summaries(limit=20, offset=0):
    """
    Pulls transaction summaries from Vintrace using REST API.
    Returns dict with results, or raises HTTPError.
    """
    url = f"{BASE_VINTRACE_URL}/{ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {VINTRACE_API_TOKEN}",
        "Accept": "application/json"
    }
    params = {
        "limit": limit,
        "offset": offset
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_vintrace_api():
    # For compatibility with DI patterns in FastAPI
    return {
        "get_transaction_summaries": get_vintrace_transaction_summaries
    }