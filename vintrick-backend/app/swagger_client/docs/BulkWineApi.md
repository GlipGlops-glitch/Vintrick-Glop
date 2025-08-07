# swagger_client.BulkWineApi

All URIs are relative to *https://oz50.vintrace.net/vinx2/api/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_available_products**](BulkWineApi.md#list_available_products) | **GET** /products/list | List available products
[**transaction_search**](BulkWineApi.md#transaction_search) | **GET** /transaction/search/ | Transaction search
[**update_a_product**](BulkWineApi.md#update_a_product) | **POST** /product-update | Update a product

# **list_available_products**
> ProductListResponse list_available_products(barcode=barcode, max=max, first=first, skip_metrics=skip_metrics)

List available products

Returns a list of all active products.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkWineApi()
barcode = 'barcode_example' # str | Can either be the vessel code or the asset ID. (optional)
max = 'max_example' # str | The starting index of results. Default: 100. (optional)
first = 'first_example' # str | The starting index of results. (optional)
skip_metrics = true # bool | False by default,if true will not include the metric data in the results. (optional)

try:
    # List available products
    api_response = api_instance.list_available_products(barcode=barcode, max=max, first=first, skip_metrics=skip_metrics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkWineApi->list_available_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Can either be the vessel code or the asset ID. | [optional] 
 **max** | **str**| The starting index of results. Default: 100. | [optional] 
 **first** | **str**| The starting index of results. | [optional] 
 **skip_metrics** | **bool**| False by default,if true will not include the metric data in the results. | [optional] 

### Return type

[**ProductListResponse**](ProductListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_search**
> TransactionSummaryResponse transaction_search(date_from=date_from, date_to=date_to, owner_name=owner_name, batch_name=batch_name, winery_name=winery_name)

Transaction search

Returns a list of all operations. These are the same transactions that get generated from Work Detail Report in vintrace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkWineApi()
date_from = 'date_from_example' # str | Format in YYYY-MM-DD format. Defaults to current date if not provided. Search for operations completed on or after this date. (optional)
date_to = 'date_to_example' # str | Format in YYYY-MM-DD format.  Defaults to current date if not provided. Search for operations completed on or before this date. (optional)
owner_name = 'owner_name_example' # str | String that matches the owner name. (optional)
batch_name = 'batch_name_example' # str | String that matches the batch name. (optional)
winery_name = 'winery_name_example' # str | String that matches the winery name. (optional)

try:
    # Transaction search
    api_response = api_instance.transaction_search(date_from=date_from, date_to=date_to, owner_name=owner_name, batch_name=batch_name, winery_name=winery_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkWineApi->transaction_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **str**| Format in YYYY-MM-DD format. Defaults to current date if not provided. Search for operations completed on or after this date. | [optional] 
 **date_to** | **str**| Format in YYYY-MM-DD format.  Defaults to current date if not provided. Search for operations completed on or before this date. | [optional] 
 **owner_name** | **str**| String that matches the owner name. | [optional] 
 **batch_name** | **str**| String that matches the batch name. | [optional] 
 **winery_name** | **str**| String that matches the winery name. | [optional] 

### Return type

[**TransactionSummaryResponse**](TransactionSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_product**
> ProductUpdateResponse update_a_product(body=body)

Update a product

To update a product, you need to provide the `productId` of the product. The propertyTypes that are available to be updated from this endpoint Grading, ProductState, Program, ProductCategory, Varietal, Region, Vintage, Description. You can query for the `propertyId` of the propertyType by using the /search endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkWineApi()
body = swagger_client.ProductUpdateData() # ProductUpdateData |  (optional)

try:
    # Update a product
    api_response = api_instance.update_a_product(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkWineApi->update_a_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductUpdateData**](ProductUpdateData.md)|  | [optional] 

### Return type

[**ProductUpdateResponse**](ProductUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

