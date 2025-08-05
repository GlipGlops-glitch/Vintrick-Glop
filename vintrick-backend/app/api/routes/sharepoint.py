# vintrick-backend/app/api/routes/sharepoint.py

from fastapi import APIRouter
import os
from dotenv import load_dotenv

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

router = APIRouter()

load_dotenv()
site_url = os.getenv("SHAREPOINT_SITE")
list_name = os.getenv("SHAREPOINT_LIST")
username = os.getenv("SHAREPOINT_USER")
password = os.getenv("SHAREPOINT_PASSWORD")

@router.get("/sharepoint/")
def get_sharepoint_items():
    ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
    sp_list = ctx.web.lists.get_by_title(list_name)
    items = sp_list.items.top(100).get().execute_query()
    # Return as list of dicts
    return [item.properties for item in items]