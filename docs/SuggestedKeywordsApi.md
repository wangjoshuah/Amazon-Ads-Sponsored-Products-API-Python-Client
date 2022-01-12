# amazon_ads_sponsored_products_client.SuggestedKeywordsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_get_asin_suggested_keywords**](SuggestedKeywordsApi.md#bulk_get_asin_suggested_keywords) | **POST** /v2/sp/asins/suggested/keywords | Gets suggested keyword for a specified list of ASINs.
[**get_ad_group_suggested_keywords**](SuggestedKeywordsApi.md#get_ad_group_suggested_keywords) | **GET** /v2/sp/adGroups/{adGroupId}/suggested/keywords | Gets suggested keywords for the specified ad group.
[**get_ad_group_suggested_keywords_ex**](SuggestedKeywordsApi.md#get_ad_group_suggested_keywords_ex) | **GET** /v2/sp/adGroups/{adGroupId}/suggested/keywords/extended | Gets suggested keywords with extended data for the specified ad group.
[**get_asin_suggested_keywords**](SuggestedKeywordsApi.md#get_asin_suggested_keywords) | **GET** /v2/sp/asins/{asinValue}/suggested/keywords | Gets suggested keywords for the specified ASIN.


# **bulk_get_asin_suggested_keywords**
> BulkGetAsinSuggestedKeywordsResponse bulk_get_asin_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets suggested keyword for a specified list of ASINs.

Suggested keywords are returned in an array ordered by descending effectiveness.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import suggested_keywords_api
from amazon_ads_sponsored_products_client.model.inline_object import InlineObject
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.bulk_get_asin_suggested_keywords_response import BulkGetAsinSuggestedKeywordsResponse
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
    api_instance = suggested_keywords_api.SuggestedKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    inline_object = InlineObject(
        asins=[
            "asins_example",
        ],
        max_num_suggestions=100,
    ) # InlineObject |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets suggested keyword for a specified list of ASINs.
        api_response = api_instance.bulk_get_asin_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SuggestedKeywordsApi->bulk_get_asin_suggested_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets suggested keyword for a specified list of ASINs.
        api_response = api_instance.bulk_get_asin_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, inline_object=inline_object)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SuggestedKeywordsApi->bulk_get_asin_suggested_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional]

### Return type

[**BulkGetAsinSuggestedKeywordsResponse**](BulkGetAsinSuggestedKeywordsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | One or more query parameters contained an invalid value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_group_suggested_keywords**
> AdGroupSuggestedKeywordsResponse get_ad_group_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Gets suggested keywords for the specified ad group.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import suggested_keywords_api
from amazon_ads_sponsored_products_client.model.ad_group_suggested_keywords_response import AdGroupSuggestedKeywordsResponse
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
    api_instance = suggested_keywords_api.SuggestedKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 3.14 # float | The identifier of a valid ad group.
    max_num_suggestions = 100 # int | The maxiumum number of suggested keywords for the response. (optional) if omitted the server will use the default value of 100
    ad_state_filter = "enabled" # str | Filters results to ad groups with state matching the comma-delimited list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets suggested keywords for the specified ad group.
        api_response = api_instance.get_ad_group_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SuggestedKeywordsApi->get_ad_group_suggested_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets suggested keywords for the specified ad group.
        api_response = api_instance.get_ad_group_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id, max_num_suggestions=max_num_suggestions, ad_state_filter=ad_state_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SuggestedKeywordsApi->get_ad_group_suggested_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_group_id** | **float**| The identifier of a valid ad group. |
 **max_num_suggestions** | **int**| The maxiumum number of suggested keywords for the response. | [optional] if omitted the server will use the default value of 100
 **ad_state_filter** | **str**| Filters results to ad groups with state matching the comma-delimited list. | [optional]

### Return type

[**AdGroupSuggestedKeywordsResponse**](AdGroupSuggestedKeywordsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | The requested resource was not found. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_group_suggested_keywords_ex**
> [AdGroupSuggestedKeywordsResponseEx] get_ad_group_suggested_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Gets suggested keywords with extended data for the specified ad group.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import suggested_keywords_api
from amazon_ads_sponsored_products_client.model.ad_group_suggested_keywords_response_ex import AdGroupSuggestedKeywordsResponseEx
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
    api_instance = suggested_keywords_api.SuggestedKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 3.14 # float | The identifier of a valid ad group.
    max_num_suggestions = 100 # int | The maxiumum number of suggested keywords for the response. (optional) if omitted the server will use the default value of 100
    suggest_bids = "no" # str | Set to `yes` to include a suggest bid for the suggested keyword in the response. Otherwise, set to `no`. (optional) if omitted the server will use the default value of "no"
    ad_state_filter = "enabled" # str | Filters results to ad groups with state matching the comma-delimited list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets suggested keywords with extended data for the specified ad group.
        api_response = api_instance.get_ad_group_suggested_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SuggestedKeywordsApi->get_ad_group_suggested_keywords_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets suggested keywords with extended data for the specified ad group.
        api_response = api_instance.get_ad_group_suggested_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id, max_num_suggestions=max_num_suggestions, suggest_bids=suggest_bids, ad_state_filter=ad_state_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SuggestedKeywordsApi->get_ad_group_suggested_keywords_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_group_id** | **float**| The identifier of a valid ad group. |
 **max_num_suggestions** | **int**| The maxiumum number of suggested keywords for the response. | [optional] if omitted the server will use the default value of 100
 **suggest_bids** | **str**| Set to &#x60;yes&#x60; to include a suggest bid for the suggested keyword in the response. Otherwise, set to &#x60;no&#x60;. | [optional] if omitted the server will use the default value of "no"
 **ad_state_filter** | **str**| Filters results to ad groups with state matching the comma-delimited list. | [optional]

### Return type

[**[AdGroupSuggestedKeywordsResponseEx]**](AdGroupSuggestedKeywordsResponseEx.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | One or more query parameters contained an invalid value. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asin_suggested_keywords**
> GetAsinSuggestedKeywordsResponse get_asin_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, asin_value)

Gets suggested keywords for the specified ASIN.

Suggested keywords are returned in an array ordered by descending effectiveness.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import suggested_keywords_api
from amazon_ads_sponsored_products_client.model.get_asin_suggested_keywords_response import GetAsinSuggestedKeywordsResponse
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
    api_instance = suggested_keywords_api.SuggestedKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    asin_value = "asinValue_example" # str | An ASIN.
    max_num_suggestions = 100 # int | The maxiumum number of suggested keywords for the response. (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # Gets suggested keywords for the specified ASIN.
        api_response = api_instance.get_asin_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, asin_value)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SuggestedKeywordsApi->get_asin_suggested_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets suggested keywords for the specified ASIN.
        api_response = api_instance.get_asin_suggested_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, asin_value, max_num_suggestions=max_num_suggestions)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SuggestedKeywordsApi->get_asin_suggested_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **asin_value** | **str**| An ASIN. |
 **max_num_suggestions** | **int**| The maxiumum number of suggested keywords for the response. | [optional] if omitted the server will use the default value of 100

### Return type

[**GetAsinSuggestedKeywordsResponse**](GetAsinSuggestedKeywordsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | One or more query parameters contained an invalid value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

