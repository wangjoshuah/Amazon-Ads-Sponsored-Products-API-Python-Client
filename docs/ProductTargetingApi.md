# amazon_ads_sponsored_products_client.ProductTargetingApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_targeting_clause**](ProductTargetingApi.md#archive_targeting_clause) | **DELETE** /v2/sp/targets/{targetId} | Archives a targeting clause.
[**create_target_recommendations**](ProductTargetingApi.md#create_target_recommendations) | **POST** /v2/sp/targets/productRecommendations | Gets a list of recommended products for targeting.
[**create_targeting_clauses**](ProductTargetingApi.md#create_targeting_clauses) | **POST** /v2/sp/targets | Creates one or more targeting expressions.
[**get_brand_recommendations**](ProductTargetingApi.md#get_brand_recommendations) | **GET** /v2/sp/targets/brands | Get recommended brands for Sponsored Products.
[**get_targeting_clause**](ProductTargetingApi.md#get_targeting_clause) | **GET** /v2/sp/targets/{targetId} | Get a targeting clause specified by identifier.
[**get_targeting_clause_ex**](ProductTargetingApi.md#get_targeting_clause_ex) | **GET** /v2/sp/targets/extended/{targetId} | Get a targeting clause specified by identifier.
[**list_targeting_clauses**](ProductTargetingApi.md#list_targeting_clauses) | **GET** /v2/sp/targets | Gets a list of targeting clauses filtered by specified criteria.
[**list_targeting_clauses_ex**](ProductTargetingApi.md#list_targeting_clauses_ex) | **GET** /v2/sp/targets/extended | Gets a list of targeting clauses filtered by specified criteria.
[**update_targeting_clause**](ProductTargetingApi.md#update_targeting_clause) | **PUT** /v2/sp/targets | Updates one or more targeting clauses.


# **archive_targeting_clause**
> TargetingClauseResponse archive_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Archives a targeting clause.

Set the `status` of a targeting clause to `archived`. Note that once a targeting clause `status` is set to `archived`, it cannot be changed.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.targeting_clause_response import TargetingClauseResponse
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 3.14 # float | The target identifier.

    # example passing only required values which don't have defaults set
    try:
        # Archives a targeting clause.
        api_response = api_instance.archive_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->archive_targeting_clause: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **target_id** | **float**| The target identifier. |

### Return type

[**TargetingClauseResponse**](TargetingClauseResponse.md)

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
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_target_recommendations**
> ProductRecommendationsResponse create_target_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of recommended products for targeting.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.inline_object2 import InlineObject2
from amazon_ads_sponsored_products_client.model.product_recommendations_response import ProductRecommendationsResponse
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    inline_object2 = InlineObject2(
        page_size=3.14,
        page_number=3.14,
        asins=[
            "asins_example",
        ],
    ) # InlineObject2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of recommended products for targeting.
        api_response = api_instance.create_target_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->create_target_recommendations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of recommended products for targeting.
        api_response = api_instance.create_target_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, inline_object2=inline_object2)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->create_target_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional]

### Return type

[**ProductRecommendationsResponse**](ProductRecommendationsResponse.md)

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

# **create_targeting_clauses**
> [TargetingClauseResponse] create_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Creates one or more targeting expressions.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.create_targeting_clause import CreateTargetingClause
from amazon_ads_sponsored_products_client.model.targeting_clause_response import TargetingClauseResponse
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_targeting_clause = [
        CreateTargetingClause(None),
    ] # [CreateTargetingClause] | A list of targeting clauses. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates one or more targeting expressions.
        api_response = api_instance.create_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->create_targeting_clauses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates one or more targeting expressions.
        api_response = api_instance.create_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_targeting_clause=create_targeting_clause)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->create_targeting_clauses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **create_targeting_clause** | [**[CreateTargetingClause]**](CreateTargetingClause.md)| A list of targeting clauses. | [optional]

### Return type

[**[TargetingClauseResponse]**](TargetingClauseResponse.md)

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

# **get_brand_recommendations**
> BrandResponse get_brand_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Get recommended brands for Sponsored Products.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.brand_response import BrandResponse
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword = "keyword_example" # str | A keyword for which to get recommended brands. (optional)
    category_id = 3.14 # float | Gets the top 50 brands for the specified category identifier. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get recommended brands for Sponsored Products.
        api_response = api_instance.get_brand_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->get_brand_recommendations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get recommended brands for Sponsored Products.
        api_response = api_instance.get_brand_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword=keyword, category_id=category_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->get_brand_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword** | **str**| A keyword for which to get recommended brands. | [optional]
 **category_id** | **float**| Gets the top 50 brands for the specified category identifier. | [optional]

### Return type

[**BrandResponse**](BrandResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_targeting_clause**
> TargetingClause get_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Get a targeting clause specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.targeting_clause import TargetingClause
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 3.14 # float | The target identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get a targeting clause specified by identifier.
        api_response = api_instance.get_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->get_targeting_clause: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **target_id** | **float**| The target identifier. |

### Return type

[**TargetingClause**](TargetingClause.md)

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

# **get_targeting_clause_ex**
> TargetingClauseEx get_targeting_clause_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Get a targeting clause specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.targeting_clause_ex import TargetingClauseEx
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 3.14 # float | The target identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get a targeting clause specified by identifier.
        api_response = api_instance.get_targeting_clause_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->get_targeting_clause_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **target_id** | **float**| The target identifier. |

### Return type

[**TargetingClauseEx**](TargetingClauseEx.md)

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

# **list_targeting_clauses**
> [TargetingClause] list_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of targeting clauses filtered by specified criteria.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.targeting_clause import TargetingClause
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    target_id_filter = "targetIdFilter_example" # str | A comma-delimited list of target identifiers. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of targeting clauses filtered by specified criteria.
        api_response = api_instance.list_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->list_targeting_clauses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of targeting clauses filtered by specified criteria.
        api_response = api_instance.list_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, target_id_filter=target_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->list_targeting_clauses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **state_filter** | **str**| Restricts results to resources with state within the specified comma-separated list. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]
 **ad_group_id_filter** | **str**| Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. | [optional]
 **target_id_filter** | **str**| A comma-delimited list of target identifiers. | [optional]

### Return type

[**[TargetingClause]**](TargetingClause.md)

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

# **list_targeting_clauses_ex**
> [TargetingClauseEx] list_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of targeting clauses filtered by specified criteria.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.targeting_clause_ex import TargetingClauseEx
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    target_id_filter = "targetIdFilter_example" # str | A comma-delimited list of target identifiers. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of targeting clauses filtered by specified criteria.
        api_response = api_instance.list_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->list_targeting_clauses_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of targeting clauses filtered by specified criteria.
        api_response = api_instance.list_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, target_id_filter=target_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->list_targeting_clauses_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **state_filter** | **str**| Restricts results to resources with state within the specified comma-separated list. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]
 **ad_group_id_filter** | **str**| Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. | [optional]
 **target_id_filter** | **str**| A comma-delimited list of target identifiers. | [optional]

### Return type

[**[TargetingClauseEx]**](TargetingClauseEx.md)

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

# **update_targeting_clause**
> [TargetingClauseResponse] update_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Updates one or more targeting clauses.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_targeting_api
from amazon_ads_sponsored_products_client.model.update_targeting_clause import UpdateTargetingClause
from amazon_ads_sponsored_products_client.model.targeting_clause_response import TargetingClauseResponse
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
    api_instance = product_targeting_api.ProductTargetingApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_targeting_clause = [
        UpdateTargetingClause(None),
    ] # [UpdateTargetingClause] | A list of targeting clauses with updated values. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates one or more targeting clauses.
        api_response = api_instance.update_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->update_targeting_clause: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates one or more targeting clauses.
        api_response = api_instance.update_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_targeting_clause=update_targeting_clause)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductTargetingApi->update_targeting_clause: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **update_targeting_clause** | [**[UpdateTargetingClause]**](UpdateTargetingClause.md)| A list of targeting clauses with updated values. | [optional]

### Return type

[**[TargetingClauseResponse]**](TargetingClauseResponse.md)

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
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

