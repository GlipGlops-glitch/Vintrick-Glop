# vintrick-backend/tools/sharepoint_fetch.py

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
import os
from dotenv import load_dotenv

# Load secrets from .env
load_dotenv()

site_url = os.getenv("SHAREPOINT_SITE")
list_name = os.getenv("SHAREPOINT_LIST")
username = os.getenv("SHAREPOINT_USER")
password = os.getenv("SHAREPOINT_PASSWORD")

ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
sp_list = ctx.web.lists.get_by_title(list_name)

# Fetch top 100 items (adjust as needed)
items = sp_list.items.top(100).get().execute_query()

print(f"Fetched {len(items)} items from SharePoint list '{list_name}'")
for item in items:
    print(item.properties)  # Dict of field names and values