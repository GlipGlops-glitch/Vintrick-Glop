# vintrick-backend/tools/fetch_shipments.py
# Usage: python tools/fetch_shipments.py
# Hardcoded to call /smwe/api/v7/operation/shipment and save to tools/data/shipments/all_shipments.json

import os
import json
import logging
from dotenv import load_dotenv
import requests

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    return logging.getLogger(__name__)

# Initialize logging
logger = setup_logging()

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

if __name__ == "__main__":
    load_dotenv()
    API_TOKEN = os.getenv("API_TOKEN")
    BASE_URL = os.getenv("BASE_URL", "https://us61.vintrace.net")

    endpoint_path = "/smwe/api/v7/operation/shipments"
    url = BASE_URL + endpoint_path

    output_dir = "tools/data/shipments"
    ensure_dir(output_dir)
    output_path = os.path.join(output_dir, "all_shipments.json")

    headers = {}
    if API_TOKEN:
        headers["Authorization"] = f"Bearer {API_TOKEN}"

    logger.info(f"Fetching all shipments from {url} ...")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ Saved all shipments to {output_path}")
    except Exception as e:
        logger.error(f"❌ Error fetching all shipments: {e}")