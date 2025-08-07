# SalesOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**invoice_date** | **str** |  | [optional] 
**invoice_date_as_text** | **str** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**send_to** | [**Party**](Party.md) |  | [optional] 
**sales_type** | **str** |  | [optional] 
**sales_price_list_id** | **int** |  | [optional] 
**sales_price_list_name** | **str** |  | [optional] 
**price_details** | [**PriceList**](PriceList.md) |  | [optional] 
**sales_order_status** | **str** |  | [optional] 
**sales_order_items** | [**list[SalesOrderItem]**](SalesOrderItem.md) |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**order_date** | **int** |  | [optional] 
**order_date_as_text** | **str** |  | [optional] 
**winery_id** | **str** |  | [optional] 
**winery_name** | **str** |  | [optional] 
**fulfillment** | **str** |  | [optional] 
**fulfillment_date** | **str** |  | [optional] 
**fulfillment_date_as_text** | **str** |  | [optional] 
**sales_region_id** | **str** |  | [optional] 
**sales_region_code** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**customer_pickup** | **bool** |  | [optional] 
**disable_accounts_sync** | **bool** |  | [optional] 
**sub_total** | **int** |  | [optional] 
**tax_breakdown** | [**list[TaxAmount]**](TaxAmount.md) |  | [optional] 
**total** | **int** |  | [optional] 
**acct_reference** | **str** |  | [optional] 
**pos_sale_reference** | **str** |  | [optional] 
**ignore_stock_error** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

