# vintrick-backend/tools/transFetch.py

import sys
import os

# Add the parent directory to sys.path so 'app' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import importlib
from app.utils.vintrace_client import VintraceSmartClient
from datetime import datetime, timedelta
from collections import deque
from threading import Lock
import time

# Setup logging
LOG_DIR = "Main/Logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "fetch.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def get_model(model_name: str):
    if not model_name:
        return None
    models_mod = importlib.import_module("app.models.models")
    return getattr(models_mod, model_name, None)


# Global deque and lock for RPM/Throughput tracking
request_times = deque()
metrics_lock = Lock()

def auto_call_endpoint(client, endpoint_key, params=None, data=None):
    ep_info = client.endpoint_map[endpoint_key]
    req_model = get_model(ep_info.get("request_schema"))
    resp_model = get_model(ep_info.get("response_schema"))

    if req_model and data:
        try:
            data = req_model(**data).dict()
        except Exception as e:
            logger.warning(f"❌ Error creating request model: {e}. Sending raw data as-is...")

    start_time = time.time()
    response = client.call_endpoint(endpoint_key, params=params, data=data)
    latency = time.time() - start_time
    # Simulate TTFB (approximate)
    ttfb = len(json.dumps(response)) / 1000.0  # bytes to kilobytes to seconds (rough estimate)

    # Update RPM and throughput
    now = time.time()
    with metrics_lock:
        request_times.append(now)
        while request_times and request_times[0] < now - 60:
            request_times.popleft()
        rpm = len(request_times)
        throughput = rpm / 60.0

    logger.info(f"📊 Metrics | Latency: {latency:.4f}s | TTFB: {ttfb:.4f}s | RPM: {rpm} | Throughput: {throughput:.2f} req/sec")

    if resp_model:
        try:
            return resp_model.model_validate(response)
        except Exception as e:
            logger.warning(f"❌ Error parsing response with model: {e}. Returning raw JSON.")
            return response
    return response

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def parallel_fetch_and_save(
    client, endpoint_key, start_date, end_date, date_param="date", extra_params=None, max_workers=5, output_root="data", error_log=None
):
    output_dir = os.path.join(output_root, endpoint_key.replace(":", "-").replace("/", "-").replace("<", "").replace(">", ""))
    ensure_dir(output_dir)

    def fetch_and_save(date_str):
        params = {date_param: date_str}
        if extra_params:
            params.update(extra_params)
        logger.info(f"Fetching {endpoint_key} for {date_param}={date_str}...")
        try:
            result = auto_call_endpoint(client, endpoint_key, params=params)
            output_path = os.path.join(output_dir, f"{date_str}.json")
            with open(output_path, "w", encoding="utf-8") as f:
                if hasattr(result, "model_dump"):
                    json.dump(result.model_dump(), f, indent=2, ensure_ascii=False)
                elif hasattr(result, "dict"):
                    json.dump(result.dict(), f, indent=2, ensure_ascii=False)
                else:
                    json.dump(result, f, indent=2, ensure_ascii=False)
            logger.info(f"✅ Saved {endpoint_key} for {date_str} to {output_path}")
            return date_str, output_path
        except Exception as e:
            logger.error(f"❌ Error fetching for {date_str}: {e}")
            return None

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    all_days = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end - start).days + 1)]

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_date = {executor.submit(fetch_and_save, day): day for day in all_days}
        for future in as_completed(future_to_date):
            day = future_to_date[future]
            try:
                result = future.result()
                if result:
                    results.append(result)
            except Exception as e:
                logger.error(f"❌ Exception in fetch_and_save for {day}: {e}")

    logger.info(f"\nAll done! {len(results)} days fetched for {endpoint_key}. Check logs for any errors.")
    return results

if __name__ == "__main__":
    # Accept parameters as a JSON string argument
    if len(sys.argv) > 1:
        params = json.loads(sys.argv[1])
        dateFrom = params.get("dateFrom")
        dateTo = params.get("dateTo")
        ownerName = params.get("ownerName")
        batchName = params.get("batchName")
        wineryName = params.get("wineryName")
        max_workers = params.get("max_workers", 1)
    else:
        print("No parameters passed. Exiting.")
        sys.exit(1)

    load_dotenv()
    API_KEY = os.getenv("API_TOKEN")
    ENDPOINT_MAP_PATH = os.getenv("ENDPOINT_MAP_PATH")

    if not API_KEY:
        logger.critical("❌ API_TOKEN not set. Make sure .env exists and contains API_TOKEN=...")
        exit(1)
    if not ENDPOINT_MAP_PATH or not os.path.exists(ENDPOINT_MAP_PATH):
        logger.critical("❌ ENDPOINT_MAP_PATH not set or file not found. Check your .env and path.")
        exit(1)

    client = VintraceSmartClient(
        api_key=API_KEY,
        endpoint_map_path=ENDPOINT_MAP_PATH
    )

    endpoint_key = "GET:/transaction/search"
    start_date = dateFrom
    end_date = dateTo

    extra_params = {}
    if ownerName:
        extra_params["ownerName"] = ownerName
    if batchName:
        extra_params["batchName"] = batchName
    if wineryName:
        extra_params["wineryName"] = wineryName

    parallel_fetch_and_save(
        client, endpoint_key,
        start_date, end_date,
        date_param="startDate",
        extra_params=extra_params,
        max_workers=max_workers,
        output_root="Main/data/"
    )