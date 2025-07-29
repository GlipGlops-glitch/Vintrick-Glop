# vintrick-backend/app/api/routes/auth.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Login endpoint"}


# vintrick-backend/app/api/routes/harvestloads.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_harvestloads():
    return ["Sample harvest load"]
