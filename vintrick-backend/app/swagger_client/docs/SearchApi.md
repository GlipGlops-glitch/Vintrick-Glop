# swagger_client.SearchApi

All URIs are relative to *https://oz50.vintrace.net/vinx2/api/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_results_for_item_type**](SearchApi.md#list_results_for_item_type) | **GET** /search/list/ | List results for item type

# **list_results_for_item_type**
> SimpleSearchResponse list_results_for_item_type(type, first=first, starts_with=starts_with, exact_match=exact_match)

List results for item type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
type = 'type_example' # str | Supported types are grading, owner, program, varietal, vintage, productState, region, block, grower, productCategory, batch, product, tank, vessel, containerEquipment, barrel, bin
first = 'first_example' # str | The starting index of results. (optional)
starts_with = 'starts_with_example' # str | String that matches the search result against the start of the name. (optional)
exact_match = true # bool | If false - we do a 'like' query where 'T-50' would return 'T-50', 'T-500'. When true it only returns 'T-50' (optional)

try:
    # List results for item type
    api_response = api_instance.list_results_for_item_type(type, first=first, starts_with=starts_with, exact_match=exact_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->list_results_for_item_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Supported types are grading, owner, program, varietal, vintage, productState, region, block, grower, productCategory, batch, product, tank, vessel, containerEquipment, barrel, bin | 
 **first** | **str**| The starting index of results. | [optional] 
 **starts_with** | **str**| String that matches the search result against the start of the name. | [optional] 
 **exact_match** | **bool**| If false - we do a &#x27;like&#x27; query where &#x27;T-50&#x27; would return &#x27;T-50&#x27;, &#x27;T-500&#x27;. When true it only returns &#x27;T-50&#x27; | [optional] 

### Return type

[**SimpleSearchResponse**](SimpleSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

