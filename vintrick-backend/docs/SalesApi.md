# swagger_client.SalesApi

All URIs are relative to *https://oz50.vintrace.net/vinx2/api/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_a_party**](SalesApi.md#create_or_update_a_party) | **POST** /party | Create or update a party
[**create_or_update_a_refund**](SalesApi.md#create_or_update_a_refund) | **POST** /refund | Create or update a refund
[**create_or_update_a_sales_order**](SalesApi.md#create_or_update_a_sales_order) | **POST** /sales-order | Create or update a sales order
[**get_party_details_by_id**](SalesApi.md#get_party_details_by_id) | **GET** /party/{id} | Get party details by id
[**get_party_details_by_name**](SalesApi.md#get_party_details_by_name) | **GET** /party/ | Get party details by name
[**get_refund_details_by_code**](SalesApi.md#get_refund_details_by_code) | **GET** /refund/ | Get refund details by code
[**get_refund_details_by_id**](SalesApi.md#get_refund_details_by_id) | **GET** /refund/{id} | Get refund details by id
[**get_sales_order_details_by_code**](SalesApi.md#get_sales_order_details_by_code) | **GET** /sales-order/ | Get sales order details by code
[**get_sales_order_details_by_id**](SalesApi.md#get_sales_order_details_by_id) | **GET** /sales-order/{id} | Get sales order details by id
[**list_available_refunds**](SalesApi.md#list_available_refunds) | **GET** /refund/list/ | List available refunds
[**list_available_sales_orders**](SalesApi.md#list_available_sales_orders) | **GET** /sales-order/list/ | List available sales orders
[**list_parties**](SalesApi.md#list_parties) | **GET** /party/list/ | List parties

# **create_or_update_a_party**
> PartyUpdateResponse create_or_update_a_party(body=body)

Create or update a party

To update a party, you need to provide the `id` of the party.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
body = swagger_client.Party() # Party |  (optional)

try:
    # Create or update a party
    api_response = api_instance.create_or_update_a_party(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->create_or_update_a_party: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Party**](Party.md)|  | [optional] 

### Return type

[**PartyUpdateResponse**](PartyUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_a_refund**
> RefundUpdateResponse create_or_update_a_refund(body=body)

Create or update a refund

To update a refund, you need to provide the `id' of the refund.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
body = swagger_client.Refund() # Refund |  (optional)

try:
    # Create or update a refund
    api_response = api_instance.create_or_update_a_refund(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->create_or_update_a_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Refund**](Refund.md)|  | [optional] 

### Return type

[**RefundUpdateResponse**](RefundUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_a_sales_order**
> SalesOrderUpdateResponse create_or_update_a_sales_order(body=body)

Create or update a sales order

For sales order with discounts and accounting integration with Xero is turned on for the customer, enter the discount as percentage value in `discountPct` field. Otherwise, if accounting integration is off, enter the discount in `adjustment` field as a dollar value. To update a sales order, you need to provide the `id' of the sales order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
body = swagger_client.SalesOrder() # SalesOrder |  (optional)

try:
    # Create or update a sales order
    api_response = api_instance.create_or_update_a_sales_order(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->create_or_update_a_sales_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SalesOrder**](SalesOrder.md)|  | [optional] 

### Return type

[**SalesOrderUpdateResponse**](SalesOrderUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party_details_by_id**
> Party get_party_details_by_id(id)

Get party details by id

Returns a single party with a given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
id = 'id_example' # str | The ID of the party.

try:
    # Get party details by id
    api_response = api_instance.get_party_details_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->get_party_details_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the party. | 

### Return type

[**Party**](Party.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party_details_by_name**
> Party get_party_details_by_name(name=name)

Get party details by name

Returns a single party with a given code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
name = 'name_example' # str | The primeName (surname) if the party is an individual or the primeName (company name) if the party is an organisation. (optional)

try:
    # Get party details by name
    api_response = api_instance.get_party_details_by_name(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->get_party_details_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The primeName (surname) if the party is an individual or the primeName (company name) if the party is an organisation. | [optional] 

### Return type

[**Party**](Party.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_details_by_code**
> Refund get_refund_details_by_code(code=code)

Get refund details by code

Returns a single refund with a given code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
code = 'code_example' # str | The refund name. (optional)

try:
    # Get refund details by code
    api_response = api_instance.get_refund_details_by_code(code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->get_refund_details_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The refund name. | [optional] 

### Return type

[**Refund**](Refund.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_details_by_id**
> Refund get_refund_details_by_id(id)

Get refund details by id

Returns a single refund with a given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
id = 'id_example' # str | The ID of the refund.

try:
    # Get refund details by id
    api_response = api_instance.get_refund_details_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->get_refund_details_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the refund. | 

### Return type

[**Refund**](Refund.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_order_details_by_code**
> SalesOrder get_sales_order_details_by_code(code=code)

Get sales order details by code

Returns a single sales order with a given code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
code = 'code_example' # str | The sales order number. (optional)

try:
    # Get sales order details by code
    api_response = api_instance.get_sales_order_details_by_code(code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->get_sales_order_details_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The sales order number. | [optional] 

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_order_details_by_id**
> SalesOrder get_sales_order_details_by_id(id)

Get sales order details by id

Returns a single sales order with a given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
id = 'id_example' # str | The ID of the sales order.

try:
    # Get sales order details by id
    api_response = api_instance.get_sales_order_details_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->get_sales_order_details_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the sales order. | 

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_refunds**
> RefundResponse list_available_refunds(max=max, first=first, starts_with=starts_with, status=status, customer_name=customer_name, start_date=start_date, end_date=end_date, sales_order_name=sales_order_name)

List available refunds

Returns a list of the first 100 refunds.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
max = 'max_example' # str | The starting index of results. (optional)
first = 'first_example' # str | The starting index of results. (optional)
starts_with = 'starts_with_example' # str | String that matches the QuickSearchResult against the start of the name. (optional)
status = 'status_example' # str | Status of the sales order: Awaiting approval, Approved. (optional)
customer_name = 'customer_name_example' # str | Customer on the sales order. (optional)
start_date = 'start_date_example' # str | Start date to filter out the results of the sales orders in YYYY-MM-DD format. (optional)
end_date = 'end_date_example' # str | End date to filter out the results of the sales orders in YYYY-MM-DD format. (optional)
sales_order_name = 'sales_order_name_example' # str | String that matches the sales order code of the refund. (optional)

try:
    # List available refunds
    api_response = api_instance.list_available_refunds(max=max, first=first, starts_with=starts_with, status=status, customer_name=customer_name, start_date=start_date, end_date=end_date, sales_order_name=sales_order_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->list_available_refunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **str**| The starting index of results. | [optional] 
 **first** | **str**| The starting index of results. | [optional] 
 **starts_with** | **str**| String that matches the QuickSearchResult against the start of the name. | [optional] 
 **status** | **str**| Status of the sales order: Awaiting approval, Approved. | [optional] 
 **customer_name** | **str**| Customer on the sales order. | [optional] 
 **start_date** | **str**| Start date to filter out the results of the sales orders in YYYY-MM-DD format. | [optional] 
 **end_date** | **str**| End date to filter out the results of the sales orders in YYYY-MM-DD format. | [optional] 
 **sales_order_name** | **str**| String that matches the sales order code of the refund. | [optional] 

### Return type

[**RefundResponse**](RefundResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_sales_orders**
> SalesOrderResponse list_available_sales_orders(max=max, first=first, starts_with=starts_with, status=status, customer_name=customer_name, start_date=start_date, end_date=end_date, inv_start_date=inv_start_date, inv_end_date=inv_end_date)

List available sales orders

Returns a list of the first 100 sales orders.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
max = 'max_example' # str | The starting index of results. (optional)
first = 'first_example' # str | The starting index of results. (optional)
starts_with = 'starts_with_example' # str | String that matches the QuickSearchResult against the start of the name. (optional)
status = 'status_example' # str | Status of the sales order: New, Approved, Payment in Progress, Paid. (optional)
customer_name = 'customer_name_example' # str | Customer on the sales order. (optional)
start_date = 'start_date_example' # str | Start date to filter out the results of the sales orders in YYYY-MM-DD format. (optional)
end_date = 'end_date_example' # str | End date to filter out the results of the sales orders in YYYY-MM-DD format. (optional)
inv_start_date = 'inv_start_date_example' # str | The starting invoiced date to filter out sales order results in YYYY-MM-DD format. (optional)
inv_end_date = 'inv_end_date_example' # str | The ending invoiced date to filter out sales order results in YYYY-MM-DD format. (optional)

try:
    # List available sales orders
    api_response = api_instance.list_available_sales_orders(max=max, first=first, starts_with=starts_with, status=status, customer_name=customer_name, start_date=start_date, end_date=end_date, inv_start_date=inv_start_date, inv_end_date=inv_end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->list_available_sales_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **str**| The starting index of results. | [optional] 
 **first** | **str**| The starting index of results. | [optional] 
 **starts_with** | **str**| String that matches the QuickSearchResult against the start of the name. | [optional] 
 **status** | **str**| Status of the sales order: New, Approved, Payment in Progress, Paid. | [optional] 
 **customer_name** | **str**| Customer on the sales order. | [optional] 
 **start_date** | **str**| Start date to filter out the results of the sales orders in YYYY-MM-DD format. | [optional] 
 **end_date** | **str**| End date to filter out the results of the sales orders in YYYY-MM-DD format. | [optional] 
 **inv_start_date** | **str**| The starting invoiced date to filter out sales order results in YYYY-MM-DD format. | [optional] 
 **inv_end_date** | **str**| The ending invoiced date to filter out sales order results in YYYY-MM-DD format. | [optional] 

### Return type

[**SalesOrderResponse**](SalesOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parties**
> PartyResponse list_parties(max=max, first=first, starts_with=starts_with, category=category)

List parties

Returns a list of the first 100 parties.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesApi()
max = 'max_example' # str | The starting index of results. Default: 100. (optional)
first = 'first_example' # str | The starting index of results. (optional)
starts_with = 'starts_with_example' # str | String that matches the primeName (Surname field in vintrace for individuals, Company Name for organisations) with the given string against the start of the name. (optional)
category = 'category_example' # str | Category of the party: All, Individuals, Organisations. (optional)

try:
    # List parties
    api_response = api_instance.list_parties(max=max, first=first, starts_with=starts_with, category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesApi->list_parties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **str**| The starting index of results. Default: 100. | [optional] 
 **first** | **str**| The starting index of results. | [optional] 
 **starts_with** | **str**| String that matches the primeName (Surname field in vintrace for individuals, Company Name for organisations) with the given string against the start of the name. | [optional] 
 **category** | **str**| Category of the party: All, Individuals, Organisations. | [optional] 

### Return type

[**PartyResponse**](PartyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

