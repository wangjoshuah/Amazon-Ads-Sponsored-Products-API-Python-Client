# amazon_ads_sponsored_products_client.NegativeKeywordsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_negative_keyword**](NegativeKeywordsApi.md#archive_negative_keyword) | **DELETE** /v2/sp/negativeKeywords/{keywordId} | Archives a negative keyword.
[**create_negative_keywords**](NegativeKeywordsApi.md#create_negative_keywords) | **POST** /v2/sp/negativeKeywords | Creates one or more negative keywords.
[**get_negative_keyword**](NegativeKeywordsApi.md#get_negative_keyword) | **GET** /v2/sp/negativeKeywords/{keywordId} | Gets a negative keyword specified by identifier.
[**get_negative_keyword_ex**](NegativeKeywordsApi.md#get_negative_keyword_ex) | **GET** /v2/sp/negativeKeywords/extended/{keywordId} | Gets a negative keyword that has extended data fields.
[**list_negative_keywords**](NegativeKeywordsApi.md#list_negative_keywords) | **GET** /v2/sp/negativeKeywords | Gets a list of negative keyword objects.
[**list_negative_keywords_ex**](NegativeKeywordsApi.md#list_negative_keywords_ex) | **GET** /v2/sp/negativeKeywords/extended | Gets a list of negative keywords that have extended data fields.
[**update_negative_keywords**](NegativeKeywordsApi.md#update_negative_keywords) | **PUT** /v2/sp/negativeKeywords | Updates one or more negative keywords.


# **archive_negative_keyword**
> NegativeKeywordResponse archive_negative_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Archives a negative keyword.

Set the status of the specified negative keyword to `archived`. Note that once the status for a keyword is set to `archived` it cannot be changed.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_keywords_api
from amazon_ads_sponsored_products_client.model.negative_keyword_response import NegativeKeywordResponse
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
    api_instance = negative_keywords_api.NegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing negative keyword.

    # example passing only required values which don't have defaults set
    try:
        # Archives a negative keyword.
        api_response = api_instance.archive_negative_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->archive_negative_keyword: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing negative keyword. |

### Return type

[**NegativeKeywordResponse**](NegativeKeywordResponse.md)

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

# **create_negative_keywords**
> [NegativeKeywordResponse] create_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Creates one or more negative keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_keywords_api
from amazon_ads_sponsored_products_client.model.negative_keyword_response import NegativeKeywordResponse
from amazon_ads_sponsored_products_client.model.create_negative_keyword import CreateNegativeKeyword
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
    api_instance = negative_keywords_api.NegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_negative_keyword = [
        CreateNegativeKeyword(None),
    ] # [CreateNegativeKeyword] | An array of negative keyword objects. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates one or more negative keywords.
        api_response = api_instance.create_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->create_negative_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates one or more negative keywords.
        api_response = api_instance.create_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_negative_keyword=create_negative_keyword)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->create_negative_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **create_negative_keyword** | [**[CreateNegativeKeyword]**](CreateNegativeKeyword.md)| An array of negative keyword objects. | [optional]

### Return type

[**[NegativeKeywordResponse]**](NegativeKeywordResponse.md)

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

# **get_negative_keyword**
> NegativeKeyword get_negative_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Gets a negative keyword specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_keywords_api
from amazon_ads_sponsored_products_client.model.negative_keyword import NegativeKeyword
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
    api_instance = negative_keywords_api.NegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing negative keyword.

    # example passing only required values which don't have defaults set
    try:
        # Gets a negative keyword specified by identifier.
        api_response = api_instance.get_negative_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->get_negative_keyword: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing negative keyword. |

### Return type

[**NegativeKeyword**](NegativeKeyword.md)

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

# **get_negative_keyword_ex**
> NegativeKeywordEx get_negative_keyword_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Gets a negative keyword that has extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_keywords_api
from amazon_ads_sponsored_products_client.model.negative_keyword_ex import NegativeKeywordEx
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
    api_instance = negative_keywords_api.NegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing negative keyword.

    # example passing only required values which don't have defaults set
    try:
        # Gets a negative keyword that has extended data fields.
        api_response = api_instance.get_negative_keyword_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->get_negative_keyword_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing negative keyword. |

### Return type

[**NegativeKeywordEx**](NegativeKeywordEx.md)

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

# **list_negative_keywords**
> [NegativeKeyword] list_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of negative keyword objects.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_keywords_api
from amazon_ads_sponsored_products_client.model.negative_keyword import NegativeKeyword
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
    api_instance = negative_keywords_api.NegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    match_type_filter = "negativePhrase" # str | Restricts results to negative keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. (optional)
    keyword_text = "keywordText_example" # str | Restricts results to negative keywords that match the specified text. (optional)
    state_filter = "enabled" # str | Restricts results to negative resources with state within the specified comma-separated list. Default includes all. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to negative keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    keyword_id_filter = "keywordIdFilter_example" # str | Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of negative keyword objects.
        api_response = api_instance.list_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->list_negative_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of negative keyword objects.
        api_response = api_instance.list_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, match_type_filter=match_type_filter, keyword_text=keyword_text, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, keyword_id_filter=keyword_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->list_negative_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **match_type_filter** | **str**| Restricts results to negative keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. | [optional]
 **keyword_text** | **str**| Restricts results to negative keywords that match the specified text. | [optional]
 **state_filter** | **str**| Restricts results to negative resources with state within the specified comma-separated list. Default includes all. | [optional]
 **campaign_id_filter** | **str**| Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]
 **ad_group_id_filter** | **str**| Restricts results to negative keywords associated with ad groups specified by identifier in the comma-delimited list. | [optional]
 **keyword_id_filter** | **str**| Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]

### Return type

[**[NegativeKeyword]**](NegativeKeyword.md)

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

# **list_negative_keywords_ex**
> [NegativeKeywordEx] list_negative_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of negative keywords that have extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_keywords_api
from amazon_ads_sponsored_products_client.model.negative_keyword_ex import NegativeKeywordEx
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
    api_instance = negative_keywords_api.NegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    match_type_filter = "negativePhrase" # str | Restricts results to negative keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. (optional)
    keyword_text = "keywordText_example" # str | Restricts results to negative keywords that match the specified text. (optional)
    state_filter = "enabled" # str | Restricts results to negative resources with state within the specified comma-separated list. Default includes all. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to negative keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    keyword_id_filter = "keywordIdFilter_example" # str | Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of negative keywords that have extended data fields.
        api_response = api_instance.list_negative_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->list_negative_keywords_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of negative keywords that have extended data fields.
        api_response = api_instance.list_negative_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, match_type_filter=match_type_filter, keyword_text=keyword_text, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, keyword_id_filter=keyword_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->list_negative_keywords_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **match_type_filter** | **str**| Restricts results to negative keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. | [optional]
 **keyword_text** | **str**| Restricts results to negative keywords that match the specified text. | [optional]
 **state_filter** | **str**| Restricts results to negative resources with state within the specified comma-separated list. Default includes all. | [optional]
 **campaign_id_filter** | **str**| Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]
 **ad_group_id_filter** | **str**| Restricts results to negative keywords associated with ad groups specified by identifier in the comma-delimited list. | [optional]
 **keyword_id_filter** | **str**| Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]

### Return type

[**[NegativeKeywordEx]**](NegativeKeywordEx.md)

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

# **update_negative_keywords**
> [NegativeKeywordResponse] update_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Updates one or more negative keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import negative_keywords_api
from amazon_ads_sponsored_products_client.model.negative_keyword_response import NegativeKeywordResponse
from amazon_ads_sponsored_products_client.model.update_negative_keyword import UpdateNegativeKeyword
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
    api_instance = negative_keywords_api.NegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_negative_keyword = [
        UpdateNegativeKeyword(None),
    ] # [UpdateNegativeKeyword] | An array negative keywords with updated values. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates one or more negative keywords.
        api_response = api_instance.update_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->update_negative_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates one or more negative keywords.
        api_response = api_instance.update_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_negative_keyword=update_negative_keyword)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling NegativeKeywordsApi->update_negative_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **update_negative_keyword** | [**[UpdateNegativeKeyword]**](UpdateNegativeKeyword.md)| An array negative keywords with updated values. | [optional]

### Return type

[**[NegativeKeywordResponse]**](NegativeKeywordResponse.md)

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

