# amazon_ads_sponsored_products_client.NegativeProductTargetingApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_negative_targeting_clause**](NegativeProductTargetingApi.md#archive_negative_targeting_clause) | **DELETE** /v2/sp/negativeTargets/{targetId} | Archives a negative targeting clause.
[**create_negative_targeting_clauses**](NegativeProductTargetingApi.md#create_negative_targeting_clauses) | **POST** /v2/sp/negativeTargets | Creates one ore more negative targeting expressions.
[**get_negative_targeting_clause**](NegativeProductTargetingApi.md#get_negative_targeting_clause) | **GET** /v2/sp/negativeTargets/{targetId} | Get a negative targeting clause specified by identifier.
[**get_negative_targeting_clause_ex**](NegativeProductTargetingApi.md#get_negative_targeting_clause_ex) | **GET** /v2/sp/negativeTargets/extended/{targetId} | Get a negative targeting clause specified by identifier.
[**list_negative_targeting_clauses**](NegativeProductTargetingApi.md#list_negative_targeting_clauses) | **GET** /v2/sp/negativeTargets | Gets a list of negative targeting clauses filtered by specified criteria.
[**list_negative_targeting_clauses_ex**](NegativeProductTargetingApi.md#list_negative_targeting_clauses_ex) | **GET** /v2/sp/negativeTargets/extended | Gets a list of negative targeting clauses filtered by specified criteria.
[**update_negative_targeting_clause**](NegativeProductTargetingApi.md#update_negative_targeting_clause) | **PUT** /v2/sp/negativeTargets | Updates one or more negative targeting clauses.


# **archive_negative_targeting_clause**
> NegativeTargetingClauseResponse archive_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Archives a negative targeting clause.

Set the `status` of a negative targeting clause to `archived`. Note that once a negative targeting clause `status` is set to `archived`, it cannot be changed.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_product_targeting_api
from amazon_ads_sponsored_products_client.model.negative_targeting_clause_response import NegativeTargetingClauseResponse
from amazon_ads_sponsored_products_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://advertising-api-test.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = amazon_ads_sponsored_products_client.Configuration(
    host = "https://advertising-api-test.amazon.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = amazon_ads_sponsored_products_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amazon_ads_sponsored_products_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = negative_product_targeting_api.NegativeProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 3.14 # float | The target identifier.

    # example passing only required values which don't have defaults set
    try:
        # Archives a negative targeting clause.
        api_response = api_instance.archive_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->archive_negative_targeting_clause: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **target_id** | **float**| The target identifier. |

### Return type

[**NegativeTargetingClauseResponse**](NegativeTargetingClauseResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_negative_targeting_clauses**
> [NegativeTargetingClauseResponse] create_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Creates one ore more negative targeting expressions.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_product_targeting_api
from amazon_ads_sponsored_products_client.model.create_negative_targeting_clause import CreateNegativeTargetingClause
from amazon_ads_sponsored_products_client.model.negative_targeting_clause_response import NegativeTargetingClauseResponse
from amazon_ads_sponsored_products_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://advertising-api-test.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = amazon_ads_sponsored_products_client.Configuration(
    host = "https://advertising-api-test.amazon.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = amazon_ads_sponsored_products_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amazon_ads_sponsored_products_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = negative_product_targeting_api.NegativeProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_negative_targeting_clause = [
        CreateNegativeTargetingClause(None),
    ] # [CreateNegativeTargetingClause] | A list of negative targeting clauses. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates one ore more negative targeting expressions.
        api_response = api_instance.create_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->create_negative_targeting_clauses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates one ore more negative targeting expressions.
        api_response = api_instance.create_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_negative_targeting_clause=create_negative_targeting_clause)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->create_negative_targeting_clauses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **create_negative_targeting_clause** | [**[CreateNegativeTargetingClause]**](CreateNegativeTargetingClause.md)| A list of negative targeting clauses. | [optional]

### Return type

[**[NegativeTargetingClauseResponse]**](NegativeTargetingClauseResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negative_targeting_clause**
> NegativeTargetingClause get_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Get a negative targeting clause specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_product_targeting_api
from amazon_ads_sponsored_products_client.model.negative_targeting_clause import NegativeTargetingClause
from amazon_ads_sponsored_products_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://advertising-api-test.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = amazon_ads_sponsored_products_client.Configuration(
    host = "https://advertising-api-test.amazon.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = amazon_ads_sponsored_products_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amazon_ads_sponsored_products_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = negative_product_targeting_api.NegativeProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 3.14 # float | The target identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get a negative targeting clause specified by identifier.
        api_response = api_instance.get_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->get_negative_targeting_clause: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **target_id** | **float**| The target identifier. |

### Return type

[**NegativeTargetingClause**](NegativeTargetingClause.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negative_targeting_clause_ex**
> NegativeTargetingClauseEx get_negative_targeting_clause_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Get a negative targeting clause specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_product_targeting_api
from amazon_ads_sponsored_products_client.model.negative_targeting_clause_ex import NegativeTargetingClauseEx
from amazon_ads_sponsored_products_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://advertising-api-test.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = amazon_ads_sponsored_products_client.Configuration(
    host = "https://advertising-api-test.amazon.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = amazon_ads_sponsored_products_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amazon_ads_sponsored_products_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = negative_product_targeting_api.NegativeProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 3.14 # float | The target identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get a negative targeting clause specified by identifier.
        api_response = api_instance.get_negative_targeting_clause_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->get_negative_targeting_clause_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **target_id** | **float**| The target identifier. |

### Return type

[**NegativeTargetingClauseEx**](NegativeTargetingClauseEx.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_negative_targeting_clauses**
> [NegativeTargetingClause] list_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of negative targeting clauses filtered by specified criteria.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_product_targeting_api
from amazon_ads_sponsored_products_client.model.negative_targeting_clause import NegativeTargetingClause
from amazon_ads_sponsored_products_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://advertising-api-test.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = amazon_ads_sponsored_products_client.Configuration(
    host = "https://advertising-api-test.amazon.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = amazon_ads_sponsored_products_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amazon_ads_sponsored_products_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = negative_product_targeting_api.NegativeProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = "enabled" # str | Restricts results to negative resources with state within the specified comma-separated list. Default includes all. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    target_id_filter = "targetIdFilter_example" # str | A comma-delimited list of target identifiers. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of negative targeting clauses filtered by specified criteria.
        api_response = api_instance.list_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->list_negative_targeting_clauses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of negative targeting clauses filtered by specified criteria.
        api_response = api_instance.list_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, target_id_filter=target_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->list_negative_targeting_clauses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **state_filter** | **str**| Restricts results to negative resources with state within the specified comma-separated list. Default includes all. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]
 **ad_group_id_filter** | **str**| Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. | [optional]
 **target_id_filter** | **str**| A comma-delimited list of target identifiers. | [optional]

### Return type

[**[NegativeTargetingClause]**](NegativeTargetingClause.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_negative_targeting_clauses_ex**
> [NegativeTargetingClauseEx] list_negative_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of negative targeting clauses filtered by specified criteria.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_product_targeting_api
from amazon_ads_sponsored_products_client.model.negative_targeting_clause_ex import NegativeTargetingClauseEx
from amazon_ads_sponsored_products_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://advertising-api-test.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = amazon_ads_sponsored_products_client.Configuration(
    host = "https://advertising-api-test.amazon.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = amazon_ads_sponsored_products_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amazon_ads_sponsored_products_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = negative_product_targeting_api.NegativeProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = "enabled" # str | Restricts results to negative resources with state within the specified comma-separated list. Default includes all. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    target_id_filter = "targetIdFilter_example" # str | A comma-delimited list of target identifiers. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of negative targeting clauses filtered by specified criteria.
        api_response = api_instance.list_negative_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->list_negative_targeting_clauses_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of negative targeting clauses filtered by specified criteria.
        api_response = api_instance.list_negative_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, target_id_filter=target_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->list_negative_targeting_clauses_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **state_filter** | **str**| Restricts results to negative resources with state within the specified comma-separated list. Default includes all. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]
 **ad_group_id_filter** | **str**| Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. | [optional]
 **target_id_filter** | **str**| A comma-delimited list of target identifiers. | [optional]

### Return type

[**[NegativeTargetingClauseEx]**](NegativeTargetingClauseEx.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_negative_targeting_clause**
> [NegativeTargetingClauseResponse] update_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Updates one or more negative targeting clauses.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_product_targeting_api
from amazon_ads_sponsored_products_client.model.negative_targeting_clause_response import NegativeTargetingClauseResponse
from amazon_ads_sponsored_products_client.model.update_negative_targeting_clause import UpdateNegativeTargetingClause
from amazon_ads_sponsored_products_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://advertising-api-test.amazon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = amazon_ads_sponsored_products_client.Configuration(
    host = "https://advertising-api-test.amazon.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = amazon_ads_sponsored_products_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amazon_ads_sponsored_products_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = negative_product_targeting_api.NegativeProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_negative_targeting_clause = [
        UpdateNegativeTargetingClause(None),
    ] # [UpdateNegativeTargetingClause] | A list of negative targeting clauses with updated values. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates one or more negative targeting clauses.
        api_response = api_instance.update_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->update_negative_targeting_clause: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates one or more negative targeting clauses.
        api_response = api_instance.update_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_negative_targeting_clause=update_negative_targeting_clause)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeProductTargetingApi->update_negative_targeting_clause: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **update_negative_targeting_clause** | [**[UpdateNegativeTargetingClause]**](UpdateNegativeTargetingClause.md)| A list of negative targeting clauses with updated values. | [optional]

### Return type

[**[NegativeTargetingClauseResponse]**](NegativeTargetingClauseResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

