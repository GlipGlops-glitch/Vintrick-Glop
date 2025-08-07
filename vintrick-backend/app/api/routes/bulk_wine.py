# vintrick-backend/app/routers/bulk_wine.py

from fastapi import APIRouter, Query, Body
import swagger_client.swagger_client as swagger_client

router = APIRouter()

configuration = swagger_client.Configuration()
api_instance = swagger_client.BulkWineApi(swagger_client.ApiClient(configuration))

@router.get("/products/list")
def list_available_products(
    barcode: str = Query(None),
    max: str = Query(None),
    first: str = Query(None),
    skip_metrics: bool = Query(False)
):
    return api_instance.list_available_products(barcode=barcode, max=max, first=first, skip_metrics=skip_metrics)

@router.get("/transaction/search/")
def transaction_search(
    date_from: str = Query(None),
    date_to: str = Query(None),
    owner_name: str = Query(None),
    batch_name: str = Query(None),
    winery_name: str = Query(None)
):
    return api_instance.transaction_search(date_from=date_from, date_to=date_to, owner_name=owner_name, batch_name=batch_name, winery_name=winery_name)

@router.post("/product-update")
def update_a_product(body: swagger_client.ProductUpdateData = Body(...)):
    return api_instance.update_a_product(body=body)