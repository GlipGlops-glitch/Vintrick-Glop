# vintrick-backend/app/routers/legacy.py

from fastapi import APIRouter, Query
import swagger_client.swagger_client as swagger_client

router = APIRouter()

configuration = swagger_client.Configuration()
api_instance = swagger_client.LegacyApi(swagger_client.ApiClient(configuration))

@router.get("/stock/lookup")
def get_stock_item_by_code_or_id(code: str = Query(None), id: str = Query(None)):
    return api_instance.get_stock_item_by_code_or_id(code=code, id=id)