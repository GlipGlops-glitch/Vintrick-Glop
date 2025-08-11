# swagger_client.JobsApi

All URIs are relative to *https://oz50.vintrace.net/vinx2/api/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_a_work_order**](JobsApi.md#assign_a_work_order) | **POST** /workorders/assign | Assign a work order
[**get_job_details_by_id**](JobsApi.md#get_job_details_by_id) | **GET** /workorders/jobs/{jobId} | Get job details by id
[**get_work_order_details_by_id_or_code**](JobsApi.md#get_work_order_details_by_id_or_code) | **GET** /workorders/{id} | Get work order details by id or code
[**list_available_work_orders**](JobsApi.md#list_available_work_orders) | **GET** /workorders/list/ | List available work orders
[**submit_job_details**](JobsApi.md#submit_job_details) | **POST** /workorders/jobs/submit | Submit job details

# **assign_a_work_order**
> AssignWorkResponse assign_a_work_order(body=body)

Assign a work order

Assign a work order to me

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
body = swagger_client.AssignWorkData() # AssignWorkData |  (optional)

try:
    # Assign a work order
    api_response = api_instance.assign_a_work_order(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->assign_a_work_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignWorkData**](AssignWorkData.md)|  | [optional] 

### Return type

[**AssignWorkResponse**](AssignWorkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_details_by_id**
> Job get_job_details_by_id(job_id)

Get job details by id

Returns a single job with a given id or code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | The ID of the job.

try:
    # Get job details by id
    api_response = api_instance.get_job_details_by_id(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job_details_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The ID of the job. | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_order_details_by_id_or_code**
> WorkOrder get_work_order_details_by_id_or_code(id, code=code)

Get work order details by id or code

Returns a single work order with a given id or code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
id = 'id_example' # str | The ID of the work order.
code = 'code_example' # str | The TWL number of the work order. (optional)

try:
    # Get work order details by id or code
    api_response = api_instance.get_work_order_details_by_id_or_code(id, code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_work_order_details_by_id_or_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the work order. | 
 **code** | **str**| The TWL number of the work order. | [optional] 

### Return type

[**WorkOrder**](WorkOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_work_orders**
> WorkOrderSearchResponse list_available_work_orders(max=max, first=first, starts_with=starts_with, assigned_to=assigned_to, work_order_state=work_order_state, from_date=from_date, to_date=to_date, count_only=count_only, winery_id=winery_id)

List available work orders

By default returns a list of all work orders that are in \"Ready\", \"In progress\", or \"Submitted\" states and are assigned to me or unassigned with a date range from 7 days ago to 3 days from now.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
max = 'max_example' # str | The starting index of results. (optional)
first = 'first_example' # str | The starting index of results. (optional)
starts_with = 'starts_with_example' # str | String that matches the QuickSearchResult against the start of the name. (optional)
assigned_to = 'assigned_to_example' # str | A high-level filter to the work order assignedTo field, from the operator's perspective. Possible values are AVAILABLE_TO_ME, ANYONE, MINE_ONLY, UNASSIGNED. Default value is AVAILABLE_TO_ME. (optional)
work_order_state = 'work_order_state_example' # str | A high-level filter for the work order status, from the operator's perspective. Possible values are ANY, IN_PROGRESS, NOT_STARTED, SUBMITTED, INCOMPLETE. Default value is ANY. (optional)
from_date = 'from_date_example' # str | Format in YYYY-MM-DD format. Search for work orders with a scheduled date on or after this date. Default value is 7 days ago. (optional)
to_date = 'to_date_example' # str | in YYYY-MM-DD format. Search for work orders with a scheduled date on or before this date. Default value is 3 days from now. (optional)
count_only = true # bool | Returns the number of results only. (optional)
winery_id = 56 # int | Winery id to filter on for work orders (optional)

try:
    # List available work orders
    api_response = api_instance.list_available_work_orders(max=max, first=first, starts_with=starts_with, assigned_to=assigned_to, work_order_state=work_order_state, from_date=from_date, to_date=to_date, count_only=count_only, winery_id=winery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->list_available_work_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **str**| The starting index of results. | [optional] 
 **first** | **str**| The starting index of results. | [optional] 
 **starts_with** | **str**| String that matches the QuickSearchResult against the start of the name. | [optional] 
 **assigned_to** | **str**| A high-level filter to the work order assignedTo field, from the operator&#x27;s perspective. Possible values are AVAILABLE_TO_ME, ANYONE, MINE_ONLY, UNASSIGNED. Default value is AVAILABLE_TO_ME. | [optional] 
 **work_order_state** | **str**| A high-level filter for the work order status, from the operator&#x27;s perspective. Possible values are ANY, IN_PROGRESS, NOT_STARTED, SUBMITTED, INCOMPLETE. Default value is ANY. | [optional] 
 **from_date** | **str**| Format in YYYY-MM-DD format. Search for work orders with a scheduled date on or after this date. Default value is 7 days ago. | [optional] 
 **to_date** | **str**| in YYYY-MM-DD format. Search for work orders with a scheduled date on or before this date. Default value is 3 days from now. | [optional] 
 **count_only** | **bool**| Returns the number of results only. | [optional] 
 **winery_id** | **int**| Winery id to filter on for work orders | [optional] 

### Return type

[**WorkOrderSearchResponse**](WorkOrderSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_job_details**
> SubmitWorkOrderStepsResponse submit_job_details(body=body)

Submit job details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
body = swagger_client.SubmitJobRequest() # SubmitJobRequest |  (optional)

try:
    # Submit job details
    api_response = api_instance.submit_job_details(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->submit_job_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmitJobRequest**](SubmitJobRequest.md)|  | [optional] 

### Return type

[**SubmitWorkOrderStepsResponse**](SubmitWorkOrderStepsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

