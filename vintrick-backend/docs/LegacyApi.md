# swagger_client.LegacyApi

All URIs are relative to *https://oz50.vintrace.net/vinx2/api/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stock_item_by_code_or_id**](LegacyApi.md#get_stock_item_by_code_or_id) | **GET** /stock/lookup | Get stock item by code or id

# **get_stock_item_by_code_or_id**
> StockItemDetails get_stock_item_by_code_or_id(code=code, id=id)

Get stock item by code or id

Returns a single stock item by code or id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LegacyApi()
code = 'code_example' # str | String that matches the code of the Stock Item matching against the start of the name. (optional)
id = 'id_example' # str | The ID of the Stock Item. (optional)

try:
    # Get stock item by code or id
    api_response = api_instance.get_stock_item_by_code_or_id(code=code, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyApi->get_stock_item_by_code_or_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| String that matches the code of the Stock Item matching against the start of the name. | [optional] 
 **id** | **str**| The ID of the Stock Item. | [optional] 

### Return type

[**StockItemDetails**](StockItemDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

