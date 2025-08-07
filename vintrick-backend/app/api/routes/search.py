# vintrick-backend/app/routers/search.py

from fastapi import APIRouter, Query
import swagger_client.swagger_client as swagger_client

router = APIRouter()

configuration = swagger_client.Configuration()
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))

@router.get("/search/list/")
def list_results_for_item_type(item_type: str = Query(None)):
    return api_instance.list_results_for_item_type(item_type=item_type)