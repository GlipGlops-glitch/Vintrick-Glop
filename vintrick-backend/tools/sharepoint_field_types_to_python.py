# vintrick-backend/tools/sharepoint_field_types_to_python.py
# Usage: python tools/sharepoint_field_types_to_python.py
# Prints SharePoint fields as Python class attributes (for models/schemas), based on their types.

import os
from dotenv import load_dotenv
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

# Type mapping from SharePoint TypeAsString to Python
TYPE_MAP = {
    "Text": "str",
    "Note": "str",
    "Number": "float",
    "Currency": "float",
    "Integer": "int",
    "Boolean": "bool",
    "DateTime": "str",  # or 'datetime' for more strict
    "Counter": "int",
    "Lookup": "str",  # or object/list for advanced use
    "User": "str",
    "Choice": "str",
    "MultiChoice": "list[str]",
    "URL": "str",
    "Attachments": "bool",
    "Computed": "str",
    "Guid": "str",
    "Calculated": "str",
    # Add more as needed
}

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

fields = sp_list.fields.get().execute_query()
print(f"# Python model/schema for SharePoint list '{list_name}':\n")
print("class SharePointItem:\n    def __init__(self):")
for field in fields:
    internal = field.properties.get("InternalName")
    dtype = field.properties.get("TypeAsString")
    pytype = TYPE_MAP.get(dtype, "str")
    print(f"        self.{internal}: {pytype} = None  # SharePoint: {dtype}")