# vintrick-backend/tools/sharepoint_field_types.py
# Usage: python tools/sharepoint_field_types.py
# Prints all fields' internal names and SharePoint data types for the configured list.

import os
from dotenv import load_dotenv
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

load_dotenv()

site_url = os.getenv("SHAREPOINT_SITE")
list_name = os.getenv("SHAREPOINT_LIST")
username = os.getenv("SHAREPOINT_USER")
password = os.getenv("SHAREPOINT_PASSWORD")

if not all([site_url, list_name, username, password]):
    print("ERROR: Missing SharePoint connection environment variables.")
    exit(1)

ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
sp_list = ctx.web.lists.get_by_title(list_name)

print(f"Fields for SharePoint list '{list_name}':\n")
fields = sp_list.fields.get().execute_query()
for field in fields:
    internal = field.properties.get("InternalName")
    dtype = field.properties.get("TypeAsString")
    title = field.properties.get("Title")
    print(f"{internal:40} | {dtype:18} | {title}")