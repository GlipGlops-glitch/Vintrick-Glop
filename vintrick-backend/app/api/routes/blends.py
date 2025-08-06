# vintrick-backend/app/api/routes/blends.py

# vintrick-backend/app/api/routes/blends.py
from fastapi import APIRouter, HTTPException, Body, Query
from typing import List
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from app.schemas.blend import BlendBase, BlendCreate, BlendOut, BlendUpdate

router = APIRouter()

# Load SharePoint creds from .env
load_dotenv()
site_url = os.getenv("SHAREPOINT_SITE")
list_name = os.getenv("SHAREPOINT_LIST")
username = os.getenv("SHAREPOINT_USER")
password = os.getenv("SHAREPOINT_PASSWORD")

# --- All fields from SharePoint, only the 5 main fields enabled ---
ALL_FIELDS = [
    "ID", "Title", "Brand", "Varietal", "Vintage", "WineType",
    # "Bulk_x0023_", "SpecSheet", "AVA", "Active", "ExpectedBottleDate",
    # "StartingRS", "TargetRS_x0028_g_x002f_L_x0029_", "Sweetener", "CuAddRate",
    # "FinishingMalic_x0028_ppm_x0029_", "FinishPVPP_x0028_ppm_x0029_",
    # "TargetCO2Min_x0028_ppm_x0029_", "TargetMaxCO2_x0028_ppm_x0029_",
    # ... (all others, commented for easy add-in)
]
ENABLED_FIELDS = [f for f in ALL_FIELDS if not f.startswith("#")]

# --- Helper to get SharePoint context/list ---
def get_sp_list():
    ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
    sp_list = ctx.web.lists.get_by_title(list_name)
    return ctx, sp_list

# --- Type conversion for SharePoint field values ---
FIELD_TYPE_MAP = {
    "ID": int,
    "Title": str,
    "Brand": str,
    "Varietal": str,
    "Vintage": str,
    "WineType": str,
    # "Alc": float,
    # "Active": str,
    # "ExpectedBottleDate": str,
    # "SpecSheet": str,
    # ... (uncomment if you enable these)
}
def convert_types(data: dict) -> dict:
    for k, v in data.items():
        if k in FIELD_TYPE_MAP and v is not None:
            try:
                data[k] = FIELD_TYPE_MAP[k](v)
            except Exception:
                data[k] = v
    return data

# --- GET all blends ---
@router.get("/blends/", response_model=List[BlendOut])
def get_blends():
    try:
        ctx, sp_list = get_sp_list()
        items = sp_list.items.top(100).select(ENABLED_FIELDS).get().execute_query()
        results = []
        for item in items:
            props = dict(item.properties)
            blend = {k: props.get(k) for k in ENABLED_FIELDS}
            results.append(BlendOut(**blend))
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SharePoint error: {str(e)}")

# --- GET blend by ID ---
@router.get("/blends/{blend_id}", response_model=BlendOut)
def get_blend_by_id(blend_id: int):
    try:
        ctx, sp_list = get_sp_list()
        item = sp_list.items.get_by_id(blend_id).get().execute_query()
        props = dict(item.properties)
        blend = {k: props.get(k) for k in ENABLED_FIELDS}
        return BlendOut(**blend)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Blend not found: {str(e)}")

# --- CREATE blend ---
@router.post("/blends/", response_model=BlendOut, status_code=201)
def create_blend(data: BlendCreate = Body(...)):
    try:
        ctx, sp_list = get_sp_list()
        data_dict = data.model_dump(exclude_unset=True)
        data_dict = convert_types(data_dict)
        create_data = {k: v for k, v in data_dict.items() if k in ENABLED_FIELDS and k != "ID"}
        item = sp_list.add_item(create_data)
        ctx.execute_query()
        new_id = item.properties.get("ID")
        # Return full blend object after creation
        item = sp_list.items.get_by_id(new_id).get().execute_query()
        props = dict(item.properties)
        blend = {k: props.get(k) for k in ENABLED_FIELDS}
        return BlendOut(**blend)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SharePoint error: {str(e)}")

# --- UPDATE blend (PATCH) ---
@router.patch("/blends/{blend_id}", response_model=BlendOut)
def update_blend(blend_id: int, data: BlendUpdate = Body(...)):
    try:
        ctx, sp_list = get_sp_list()
        item = sp_list.items.get_by_id(blend_id)
        data_dict = data.model_dump(exclude_unset=True)
        data_dict = convert_types(data_dict)
        updated_fields = {k: v for k, v in data_dict.items() if k in ENABLED_FIELDS and k != "ID"}
        for key, value in updated_fields.items():
            item.set_property(key, value)
        item.update()
        ctx.execute_query()
        # Return updated blend object
        item = sp_list.items.get_by_id(blend_id).get().execute_query()
        props = dict(item.properties)
        blend = {k: props.get(k) for k in ENABLED_FIELDS}
        return BlendOut(**blend)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SharePoint error: {str(e)}")

# --- DELETE blend ---
@router.delete("/blends/{blend_id}", response_model=dict)
def delete_blend(blend_id: int):
    try:
        ctx, sp_list = get_sp_list()
        item = sp_list.items.get_by_id(blend_id)
        item.delete_object()
        ctx.execute_query()
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Blend not found or already deleted: {str(e)}")