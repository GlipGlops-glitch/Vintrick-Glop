# swagger_client.StockApi

All URIs are relative to *https://oz50.vintrace.net/vinx2/api/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_a_note**](StockApi.md#add_a_note) | **POST** /mrp/stock/{id}/notes | Add a Note
[**list_available_stock**](StockApi.md#list_available_stock) | **GET** /inventory/ | List available stock
[**update_a_note**](StockApi.md#update_a_note) | **POST** /mrp/stock/{id}/notes/{noteId}/updates | Update a Note
[**view_a_single_note**](StockApi.md#view_a_single_note) | **GET** /mrp/stock/{id}/notes/{noteId} | View a single Note
[**view_a_single_stock_item**](StockApi.md#view_a_single_stock_item) | **GET** /mrp/stock/{id} | View a single stock item
[**view_all_notes**](StockApi.md#view_all_notes) | **GET** /mrp/stock/{id}/notes | View all notes
[**view_bulk_product_details**](StockApi.md#view_bulk_product_details) | **GET** /mrp/stock/{id}/bulk-info | View bulk product details
[**view_distribtutions**](StockApi.md#view_distribtutions) | **GET** /mrp/stock/{id}/distributions/ | View distribtutions
[**view_history_items**](StockApi.md#view_history_items) | **GET** /mrp/stock/{id}/history-items | View History items
[**view_list_of_details_fields**](StockApi.md#view_list_of_details_fields) | **GET** /mrp/stock/{id}/fields/ | View list of details fields
[**view_raw_components**](StockApi.md#view_raw_components) | **GET** /mrp/stock/{id}/raw-components | View raw components

# **add_a_note**
> InlineResponse2001 add_a_note(id, body=body)

Add a Note

Add a note to a stock item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 'id_example' # str | 
body = swagger_client.StockNote() # StockNote |  (optional)

try:
    # Add a Note
    api_response = api_instance.add_a_note(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->add_a_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**StockNote**](StockNote.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_stock**
> InventorySummaryResponse list_available_stock(max=max, first=first, _date=_date, stock_type=stock_type, owner_name=owner_name, show_equivalent_type=show_equivalent_type, breakout_costing=breakout_costing, disable_commit_headers=disable_commit_headers)

List available stock

Returns a list of all stock items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
max = 'max_example' # str | The starting index of results. (optional)
first = 'first_example' # str | The starting index of results. (optional)
_date = '_date_example' # str | The date to report stock up to, excluding stock changes done after it in YYYY-MM-DD format. (optional)
stock_type = 'stock_type_example' # str | String that matches the Stock Type of the Stock Items. Possible values are Additive, Closure, Glass/Container, Other, Wine batch, Single x1, Case x3, Case x, Case x12, Case x2, Pallet (full), Dry goods. (optional)
owner_name = 'owner_name_example' # str | String that matches the Owner's name on the Stock Items. (optional)
show_equivalent_type = 'show_equivalent_type_example' # str | Displays the ratio of what the inventory item's volume/qty is equivalent to the given showEquivalentType Possible values 750ml bottle, 375ml bottle, 9L case (dozen), 4.5L case, Litres. (optional)
breakout_costing = true # bool | When true, this retrieves each costing's category of costs and details each types cost. User needs \"Can view costs\" permission to view the costs. (optional)
disable_commit_headers = true # bool | When true, does not show an item's committed stock amount details. (optional)

try:
    # List available stock
    api_response = api_instance.list_available_stock(max=max, first=first, _date=_date, stock_type=stock_type, owner_name=owner_name, show_equivalent_type=show_equivalent_type, breakout_costing=breakout_costing, disable_commit_headers=disable_commit_headers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->list_available_stock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **str**| The starting index of results. | [optional] 
 **first** | **str**| The starting index of results. | [optional] 
 **_date** | **str**| The date to report stock up to, excluding stock changes done after it in YYYY-MM-DD format. | [optional] 
 **stock_type** | **str**| String that matches the Stock Type of the Stock Items. Possible values are Additive, Closure, Glass/Container, Other, Wine batch, Single x1, Case x3, Case x, Case x12, Case x2, Pallet (full), Dry goods. | [optional] 
 **owner_name** | **str**| String that matches the Owner&#x27;s name on the Stock Items. | [optional] 
 **show_equivalent_type** | **str**| Displays the ratio of what the inventory item&#x27;s volume/qty is equivalent to the given showEquivalentType Possible values 750ml bottle, 375ml bottle, 9L case (dozen), 4.5L case, Litres. | [optional] 
 **breakout_costing** | **bool**| When true, this retrieves each costing&#x27;s category of costs and details each types cost. User needs \&quot;Can view costs\&quot; permission to view the costs. | [optional] 
 **disable_commit_headers** | **bool**| When true, does not show an item&#x27;s committed stock amount details. | [optional] 

### Return type

[**InventorySummaryResponse**](InventorySummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_note**
> InlineResponse2001 update_a_note(id, note_id, body=body)

Update a Note

Update a note attached to a stock item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 1.2 # float | id of the note
note_id = 1.2 # float | id of the note
body = swagger_client.StockNote() # StockNote |  (optional)

try:
    # Update a Note
    api_response = api_instance.update_a_note(id, note_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->update_a_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| id of the note | 
 **note_id** | **float**| id of the note | 
 **body** | [**StockNote**](StockNote.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_a_single_note**
> StockNote view_a_single_note(id, note_id)

View a single Note

View a note for a stock item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 1.2 # float | id of the note
note_id = 1.2 # float | id of the note

try:
    # View a single Note
    api_response = api_instance.view_a_single_note(id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->view_a_single_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| id of the note | 
 **note_id** | **float**| id of the note | 

### Return type

[**StockNote**](StockNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_a_single_stock_item**
> StockItem view_a_single_stock_item(id, expand=expand)

View a single stock item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 1.2 # float | Stock item id
expand = 'expand_example' # str | Comma separated list of the details that you want to expand. Possible values are `fields`, `distributions`, `notes`, `historyItems`, `rawComponents`, `bulkInfo` (optional)

try:
    # View a single stock item
    api_response = api_instance.view_a_single_stock_item(id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->view_a_single_stock_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Stock item id | 
 **expand** | **str**| Comma separated list of the details that you want to expand. Possible values are &#x60;fields&#x60;, &#x60;distributions&#x60;, &#x60;notes&#x60;, &#x60;historyItems&#x60;, &#x60;rawComponents&#x60;, &#x60;bulkInfo&#x60; | [optional] 

### Return type

[**StockItem**](StockItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_all_notes**
> StockNotesDetail view_all_notes(id, first_result=first_result, max_result=max_result)

View all notes

A paginated list of notes for a stock item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 'id_example' # str | 
first_result = 1.2 # float |  (optional)
max_result = 1.2 # float |  (optional)

try:
    # View all notes
    api_response = api_instance.view_all_notes(id, first_result=first_result, max_result=max_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->view_all_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **first_result** | **float**|  | [optional] 
 **max_result** | **float**|  | [optional] 

### Return type

[**StockNotesDetail**](StockNotesDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_bulk_product_details**
> StockBulkInfoDetail view_bulk_product_details(id)

View bulk product details

Returns details like metrics, compositions, allergens and additives (from last bottling) about the bulk product linked to a stock item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 1.2 # float | 

try:
    # View bulk product details
    api_response = api_instance.view_bulk_product_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->view_bulk_product_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**StockBulkInfoDetail**](StockBulkInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_distribtutions**
> StockDistributionDetail view_distribtutions(id)

View distribtutions

Returns a list of distributions for a stock item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 1.2 # float | Stock item id

try:
    # View distribtutions
    api_response = api_instance.view_distribtutions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->view_distribtutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Stock item id | 

### Return type

[**StockDistributionDetail**](StockDistributionDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_history_items**
> StockHistoryItemsDetail view_history_items(id, first_result, max_result)

View History items

A paginated list of history items for a stock item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 1.2 # float | Stock item id
first_result = 1.2 # float | 
max_result = 1.2 # float | 

try:
    # View History items
    api_response = api_instance.view_history_items(id, first_result, max_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->view_history_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Stock item id | 
 **first_result** | **float**|  | 
 **max_result** | **float**|  | 

### Return type

[**StockHistoryItemsDetail**](StockHistoryItemsDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_list_of_details_fields**
> StockFieldsDetail view_list_of_details_fields(id)

View list of details fields

Returns a list of detail fields for a stock item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 1.2 # float | Stock item id

try:
    # View list of details fields
    api_response = api_instance.view_list_of_details_fields(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->view_list_of_details_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Stock item id | 

### Return type

[**StockFieldsDetail**](StockFieldsDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_raw_components**
> StockRawComponentsDetail view_raw_components(id)

View raw components

Returns a paginated list of raw components for a stock item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StockApi()
id = 1.2 # float | 

try:
    # View raw components
    api_response = api_instance.view_raw_components(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->view_raw_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**StockRawComponentsDetail**](StockRawComponentsDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

