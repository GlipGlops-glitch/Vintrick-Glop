# vintrick-backend/app/routers/sales.py

from fastapi import APIRouter, Body, Path, Query
import swagger_client.swagger_client as swagger_client

router = APIRouter()

configuration = swagger_client.Configuration()
api_instance = swagger_client.SalesApi(swagger_client.ApiClient(configuration))

@router.post("/party")
def create_or_update_a_party(body: swagger_client.Party = Body(...)):
    return api_instance.create_or_update_a_party(body=body)

@router.post("/refund")
def create_or_update_a_refund(body: swagger_client.Refund = Body(...)):
    return api_instance.create_or_update_a_refund(body=body)

@router.post("/sales-order")
def create_or_update_a_sales_order(body: swagger_client.SalesOrder = Body(...)):
    return api_instance.create_or_update_a_sales_order(body=body)

@router.get("/party/{id}")
def get_party_details_by_id(id: str = Path(...)):
    return api_instance.get_party_details_by_id(id=id)

@router.get("/party/")
def get_party_details_by_name(name: str = Query(None)):
    return api_instance.get_party_details_by_name(name=name)

@router.get("/refund/")
def get_refund_details_by_code(code: str = Query(None)):
    return api_instance.get_refund_details_by_code(code=code)

@router.get("/refund/{id}")
def get_refund_details_by_id(id: str = Path(...)):
    return api_instance.get_refund_details_by_id(id=id)

@router.get("/sales-order/")
def get_sales_order_details_by_code(code: str = Query(None)):
    return api_instance.get_sales_order_details_by_code(code=code)

@router.get("/sales-order/{id}")
def get_sales_order_details_by_id(id: str = Path(...)):
    return api_instance.get_sales_order_details_by_id(id=id)

@router.get("/refund/list/")
def list_available_refunds():
    return api_instance.list_available_refunds()

@router.get("/sales-order/list/")
def list_available_sales_orders():
    return api_instance.list_available_sales_orders()

@router.get("/party/list/")
def list_parties():
    return api_instance.list_parties()