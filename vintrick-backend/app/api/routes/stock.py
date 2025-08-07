# vintrick-backend/app/routers/stock.py

from fastapi import APIRouter, Body, Path
import swagger_client.swagger_client as swagger_client

router = APIRouter()

configuration = swagger_client.Configuration()
api_instance = swagger_client.StockApi(swagger_client.ApiClient(configuration))

@router.post("/mrp/stock/{id}/notes")
def add_a_note(id: str = Path(...), body: swagger_client.StockNote = Body(...)):
    return api_instance.add_a_note(id=id, body=body)

@router.get("/inventory/")
def list_available_stock():
    return api_instance.list_available_stock()

@router.post("/mrp/stock/{id}/notes/{noteId}/updates")
def update_a_note(id: str = Path(...), noteId: str = Path(...), body: swagger_client.StockNote = Body(...)):
    return api_instance.update_a_note(id=id, noteId=noteId, body=body)

@router.get("/mrp/stock/{id}/notes/{noteId}")
def view_a_single_note(id: str = Path(...), noteId: str = Path(...)):
    return api_instance.view_a_single_note(id=id, noteId=noteId)

@router.get("/mrp/stock/{id}")
def view_a_single_stock_item(id: str = Path(...)):
    return api_instance.view_a_single_stock_item(id=id)

@router.get("/mrp/stock/{id}/notes")
def view_all_notes(id: str = Path(...)):
    return api_instance.view_all_notes(id=id)

@router.get("/mrp/stock/{id}/bulk-info")
def view_bulk_product_details(id: str = Path(...)):
    return api_instance.view_bulk_product_details(id=id)

@router.get("/mrp/stock/{id}/distributions/")
def view_distribtutions(id: str = Path(...)):
    return api_instance.view_distribtutions(id=id)

@router.get("/mrp/stock/{id}/history-items")
def view_history_items(id: str = Path(...)):
    return api_instance.view_history_items(id=id)

@router.get("/mrp/stock/{id}/fields/")
def view_list_of_details_fields(id: str = Path(...)):
    return api_instance.view_list_of_details_fields(id=id)

@router.get("/mrp/stock/{id}/raw-components")
def view_raw_components(id: str = Path(...)):
    return api_instance.view_raw_components(id=id)