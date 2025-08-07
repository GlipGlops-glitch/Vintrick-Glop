# vintrick-backend/app/api/routes/meta.py

from fastapi import APIRouter
from app.utils.Vintrace_params import VINTRACE_TRANSACTION_SEARCH_PARAMS

router = APIRouter()

@router.get("/transaction-search-params", tags=["meta"])
def get_transaction_search_params():
    """
    Returns metadata for /transaction/search/ query parameters
    """
    return {"params": VINTRACE_TRANSACTION_SEARCH_PARAMS}