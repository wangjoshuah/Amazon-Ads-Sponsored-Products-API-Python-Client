# amazon_ads_sponsored_products_client.KeywordsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_keyword**](KeywordsApi.md#archive_keyword) | **DELETE** /v2/sp/keywords/{keywordId} | Archives a keyword.
[**create_keywords**](KeywordsApi.md#create_keywords) | **POST** /v2/sp/keywords | Creates one or more keywords.
[**get_keyword**](KeywordsApi.md#get_keyword) | **GET** /v2/sp/keywords/{keywordId} | Gets a keyword specified by identifier.
[**get_keyword_ex**](KeywordsApi.md#get_keyword_ex) | **GET** /v2/sp/keywords/extended/{keywordId} | Gets a keyword with extended data fields.
[**list_keywords**](KeywordsApi.md#list_keywords) | **GET** /v2/sp/keywords | 
[**list_keywords_ex**](KeywordsApi.md#list_keywords_ex) | **GET** /v2/sp/keywords/extended | Gets a list of keywords that have extended data fields.
[**update_keywords**](KeywordsApi.md#update_keywords) | **PUT** /v2/sp/keywords | Updates one or more keywords.


# **archive_keyword**
> KeywordResponse archive_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Archives a keyword.

Set the status of the specified keyword to `archived`. Note that once the status for a keyword is set to `archived` it cannot be changed.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import keywords_api
from amazon_ads_sponsored_products_client.model.keyword_response import KeywordResponse
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
    api_instance = keywords_api.KeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing keyword.

    # example passing only required values which don't have defaults set
    try:
        # Archives a keyword.
        api_response = api_instance.archive_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->archive_keyword: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing keyword. |

### Return type

[**KeywordResponse**](KeywordResponse.md)

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

# **create_keywords**
> [KeywordResponse] create_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Creates one or more keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import keywords_api
from amazon_ads_sponsored_products_client.model.keyword_response import KeywordResponse
from amazon_ads_sponsored_products_client.model.create_keyword import CreateKeyword
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
    api_instance = keywords_api.KeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_keyword = [
        CreateKeyword(None),
    ] # [CreateKeyword] | An array of keyword objects. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates one or more keywords.
        api_response = api_instance.create_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->create_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates one or more keywords.
        api_response = api_instance.create_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_keyword=create_keyword)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->create_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **create_keyword** | [**[CreateKeyword]**](CreateKeyword.md)| An array of keyword objects. | [optional]

### Return type

[**[KeywordResponse]**](KeywordResponse.md)

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

# **get_keyword**
> Keyword get_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Gets a keyword specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import keywords_api
from amazon_ads_sponsored_products_client.model.keyword import Keyword
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
    api_instance = keywords_api.KeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing keyword.
    locale = "locale_example" # str | The locale preference of the advertiser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a keyword specified by identifier.
        api_response = api_instance.get_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->get_keyword: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a keyword specified by identifier.
        api_response = api_instance.get_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id, locale=locale)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->get_keyword: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing keyword. |
 **locale** | **str**| The locale preference of the advertiser. | [optional]

### Return type

[**Keyword**](Keyword.md)

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

# **get_keyword_ex**
> KeywordEx get_keyword_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Gets a keyword with extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import keywords_api
from amazon_ads_sponsored_products_client.model.keyword_ex import KeywordEx
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
    api_instance = keywords_api.KeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing keyword.
    locale = "locale_example" # str | The locale preference of the advertiser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a keyword with extended data fields.
        api_response = api_instance.get_keyword_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->get_keyword_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a keyword with extended data fields.
        api_response = api_instance.get_keyword_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id, locale=locale)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->get_keyword_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing keyword. |
 **locale** | **str**| The locale preference of the advertiser. | [optional]

### Return type

[**KeywordEx**](KeywordEx.md)

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

# **list_keywords**
> [Keyword] list_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)



Gets a list of keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import keywords_api
from amazon_ads_sponsored_products_client.model.keyword import Keyword
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
    api_instance = keywords_api.KeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    match_type_filter = "broad" # str | Restricts results to keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. (optional)
    keyword_text = "keywordText_example" # str | Restricts results to keywords that match the specified text exactly. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    keyword_id_filter = "keywordIdFilter_example" # str | Restricts results to keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)
    locale = "locale_example" # str | Restricts results to keywords associated with locale. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->list_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, match_type_filter=match_type_filter, keyword_text=keyword_text, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, keyword_id_filter=keyword_id_filter, locale=locale)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->list_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **match_type_filter** | **str**| Restricts results to keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. | [optional]
 **keyword_text** | **str**| Restricts results to keywords that match the specified text exactly. | [optional]
 **state_filter** | **str**| Restricts results to resources with state within the specified comma-separated list. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]
 **ad_group_id_filter** | **str**| Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. | [optional]
 **keyword_id_filter** | **str**| Restricts results to keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]
 **locale** | **str**| Restricts results to keywords associated with locale. | [optional]

### Return type

[**[Keyword]**](Keyword.md)

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

# **list_keywords_ex**
> [KeywordEx] list_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of keywords that have extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import keywords_api
from amazon_ads_sponsored_products_client.model.keyword_ex import KeywordEx
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
    api_instance = keywords_api.KeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    match_type_filter = "broad" # str | Restricts results to keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. (optional)
    keyword_text = "keywordText_example" # str | Restricts results to keywords that match the specified text exactly. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    keyword_id_filter = "keywordIdFilter_example" # str | Restricts results to keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)
    locale = "locale_example" # str | Restricts results to keywords associated with locale. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of keywords that have extended data fields.
        api_response = api_instance.list_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->list_keywords_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of keywords that have extended data fields.
        api_response = api_instance.list_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, match_type_filter=match_type_filter, keyword_text=keyword_text, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, keyword_id_filter=keyword_id_filter, locale=locale)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->list_keywords_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **match_type_filter** | **str**| Restricts results to keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. | [optional]
 **keyword_text** | **str**| Restricts results to keywords that match the specified text exactly. | [optional]
 **state_filter** | **str**| Restricts results to resources with state within the specified comma-separated list. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]
 **ad_group_id_filter** | **str**| Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. | [optional]
 **keyword_id_filter** | **str**| Restricts results to keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]
 **locale** | **str**| Restricts results to keywords associated with locale. | [optional]

### Return type

[**[KeywordEx]**](KeywordEx.md)

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

# **update_keywords**
> [KeywordResponse] update_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Updates one or more keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import keywords_api
from amazon_ads_sponsored_products_client.model.update_keyword import UpdateKeyword
from amazon_ads_sponsored_products_client.model.keyword_response import KeywordResponse
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
    api_instance = keywords_api.KeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_keyword = [
        UpdateKeyword(None),
    ] # [UpdateKeyword] | An array of update keyword objects. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates one or more keywords.
        api_response = api_instance.update_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->update_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates one or more keywords.
        api_response = api_instance.update_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_keyword=update_keyword)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling KeywordsApi->update_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **update_keyword** | [**[UpdateKeyword]**](UpdateKeyword.md)| An array of update keyword objects. | [optional]

### Return type

[**[KeywordResponse]**](KeywordResponse.md)

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

