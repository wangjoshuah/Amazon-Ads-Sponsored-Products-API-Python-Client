# amazon_ads_sponsored_products_client.BidRecommendationsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_keyword_bid_recommendations**](BidRecommendationsApi.md#create_keyword_bid_recommendations) | **POST** /v2/sp/keywords/bidRecommendations | Gets bid recommendations for keywords.
[**get_ad_group_bid_recommendations**](BidRecommendationsApi.md#get_ad_group_bid_recommendations) | **GET** /v2/sp/adGroups/{adGroupId}/bidRecommendations | Gets a bid recommendation for an ad group.
[**get_bid_recommendations**](BidRecommendationsApi.md#get_bid_recommendations) | **POST** /v2/sp/targets/bidRecommendations | Gets a list of bid recommendations for keyword, product, or auto targeting expressions.
[**get_keyword_bid_recommendations**](BidRecommendationsApi.md#get_keyword_bid_recommendations) | **GET** /v2/sp/keywords/{keywordId}/bidRecommendations | Gets a bid recommendation for a keyword.


# **create_keyword_bid_recommendations**
> BidRecommendationsResponse create_keyword_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets bid recommendations for keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import bid_recommendations_api
from amazon_ads_sponsored_products_client.model.keyword_bid_recommendations_data import KeywordBidRecommendationsData
from amazon_ads_sponsored_products_client.model.bid_recommendations_response import BidRecommendationsResponse
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
    api_instance = bid_recommendations_api.BidRecommendationsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_bid_recommendations_data = KeywordBidRecommendationsData(None) # KeywordBidRecommendationsData | An array of keyword bid recommendation objects. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets bid recommendations for keywords.
        api_response = api_instance.create_keyword_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling BidRecommendationsApi->create_keyword_bid_recommendations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets bid recommendations for keywords.
        api_response = api_instance.create_keyword_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_bid_recommendations_data=keyword_bid_recommendations_data)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling BidRecommendationsApi->create_keyword_bid_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_bid_recommendations_data** | [**KeywordBidRecommendationsData**](KeywordBidRecommendationsData.md)| An array of keyword bid recommendation objects. | [optional]

### Return type

[**BidRecommendationsResponse**](BidRecommendationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. |  -  |
**400** | Bad request. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_group_bid_recommendations**
> AdGroupBidRecommendationsResponse get_ad_group_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Gets a bid recommendation for an ad group.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import bid_recommendations_api
from amazon_ads_sponsored_products_client.model.ad_group_bid_recommendations_response import AdGroupBidRecommendationsResponse
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
    api_instance = bid_recommendations_api.BidRecommendationsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 3.14 # float | The identifier of an existing ad group.

    # example passing only required values which don't have defaults set
    try:
        # Gets a bid recommendation for an ad group.
        api_response = api_instance.get_ad_group_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling BidRecommendationsApi->get_ad_group_bid_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_group_id** | **float**| The identifier of an existing ad group. |

### Return type

[**AdGroupBidRecommendationsResponse**](AdGroupBidRecommendationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**404** | Either the specified ad group identifier was not found, or the specified ad group was found but no associated bid was found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bid_recommendations**
> InlineResponse200 get_bid_recommendations()

Gets a list of bid recommendations for keyword, product, or auto targeting expressions.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import bid_recommendations_api
from amazon_ads_sponsored_products_client.model.inline_response200 import InlineResponse200
from amazon_ads_sponsored_products_client.model.inline_object1 import InlineObject1
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
    api_instance = bid_recommendations_api.BidRecommendationsApi(api_client)
    inline_object1 = InlineObject1(
        ad_group_id=3.14,
        expressions=[
            [
                TargetingExpressionPredicate(None),
            ],
        ],
    ) # InlineObject1 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of bid recommendations for keyword, product, or auto targeting expressions.
        api_response = api_instance.get_bid_recommendations(inline_object1=inline_object1)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling BidRecommendationsApi->get_bid_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keyword_bid_recommendations**
> KeywordBidRecommendationsResponse get_keyword_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Gets a bid recommendation for a keyword.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import bid_recommendations_api
from amazon_ads_sponsored_products_client.model.keyword_bid_recommendations_response import KeywordBidRecommendationsResponse
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
    api_instance = bid_recommendations_api.BidRecommendationsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing keyword.

    # example passing only required values which don't have defaults set
    try:
        # Gets a bid recommendation for a keyword.
        api_response = api_instance.get_keyword_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling BidRecommendationsApi->get_keyword_bid_recommendations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing keyword. |

### Return type

[**KeywordBidRecommendationsResponse**](KeywordBidRecommendationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

