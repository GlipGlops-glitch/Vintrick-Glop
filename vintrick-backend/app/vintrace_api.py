import os
from swagger_client import ApiClient, DefaultApi  # Change DefaultApi to the correct API class if needed
from swagger_client.swagger_client.configuration import Configuration

def get_vintrace_api():
    # Load token from env or .env file
    token = os.getenv("VINTRACE_API_TOKEN", "your-default-token")
    config = Configuration()
    config.api_key['Authorization'] = f"Bearer {token}"
    api_client = ApiClient(configuration=config)
    return DefaultApi(api_client)  # Change to your actual API class