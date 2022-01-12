# amazon_ads_sponsored_products_client.CampaignNegativeKeywordsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_campaign_negative_keyword**](CampaignNegativeKeywordsApi.md#archive_campaign_negative_keyword) | **DELETE** /v2/sp/campaignNegativeKeywords/{keywordId} | Archives a campaign negative keyword.
[**create_campaign_negative_keywords**](CampaignNegativeKeywordsApi.md#create_campaign_negative_keywords) | **POST** /v2/sp/campaignNegativeKeywords | Creates one or more campaign negative keywords.
[**get_campaign_negative_keyword**](CampaignNegativeKeywordsApi.md#get_campaign_negative_keyword) | **GET** /v2/sp/campaignNegativeKeywords/{keywordId} | Gets a campaign negative keyword specified by identifier.
[**get_campaign_negative_keyword_ex**](CampaignNegativeKeywordsApi.md#get_campaign_negative_keyword_ex) | **GET** /v2/sp/campaignNegativeKeywords/extended/{keywordId} | Gets a campaign negative keyword that has extended data fields.
[**list_campaign_negative_keywords**](CampaignNegativeKeywordsApi.md#list_campaign_negative_keywords) | **GET** /v2/sp/campaignNegativeKeywords | Gets a list of campaign negative keywords.
[**list_campaign_negative_keywords_ex**](CampaignNegativeKeywordsApi.md#list_campaign_negative_keywords_ex) | **GET** /v2/sp/campaignNegativeKeywords/extended | Gets a list of campaign negative keywords that have extended data fields.
[**update_campaign_negative_keywords**](CampaignNegativeKeywordsApi.md#update_campaign_negative_keywords) | **PUT** /v2/sp/campaignNegativeKeywords | Updates one or more campaign negative keywords.


# **archive_campaign_negative_keyword**
> CampaignNegativeKeywordResponse archive_campaign_negative_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Archives a campaign negative keyword.

Set the status of the specified campaign negative keyword to `archived`. Note that once the status for a keyword is set to `archived` it cannot be changed.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaign_negative_keywords_api
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.campaign_negative_keyword_response import CampaignNegativeKeywordResponse
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
    api_instance = campaign_negative_keywords_api.CampaignNegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing campaign negative keyword.

    # example passing only required values which don't have defaults set
    try:
        # Archives a campaign negative keyword.
        api_response = api_instance.archive_campaign_negative_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->archive_campaign_negative_keyword: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing campaign negative keyword. |

### Return type

[**CampaignNegativeKeywordResponse**](CampaignNegativeKeywordResponse.md)

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

# **create_campaign_negative_keywords**
> [CampaignNegativeKeywordResponse] create_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Creates one or more campaign negative keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaign_negative_keywords_api
from amazon_ads_sponsored_products_client.model.create_campaign_negative_keyword import CreateCampaignNegativeKeyword
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.campaign_negative_keyword_response import CampaignNegativeKeywordResponse
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
    api_instance = campaign_negative_keywords_api.CampaignNegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_campaign_negative_keyword = [
        CreateCampaignNegativeKeyword(None),
    ] # [CreateCampaignNegativeKeyword] | An array of campaign negative keyword objects. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates one or more campaign negative keywords.
        api_response = api_instance.create_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->create_campaign_negative_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates one or more campaign negative keywords.
        api_response = api_instance.create_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_campaign_negative_keyword=create_campaign_negative_keyword)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->create_campaign_negative_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **create_campaign_negative_keyword** | [**[CreateCampaignNegativeKeyword]**](CreateCampaignNegativeKeyword.md)| An array of campaign negative keyword objects. | [optional]

### Return type

[**[CampaignNegativeKeywordResponse]**](CampaignNegativeKeywordResponse.md)

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

# **get_campaign_negative_keyword**
> CampaignNegativeKeyword get_campaign_negative_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Gets a campaign negative keyword specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaign_negative_keywords_api
from amazon_ads_sponsored_products_client.model.campaign_negative_keyword import CampaignNegativeKeyword
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
    api_instance = campaign_negative_keywords_api.CampaignNegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing campaign negative keyword.

    # example passing only required values which don't have defaults set
    try:
        # Gets a campaign negative keyword specified by identifier.
        api_response = api_instance.get_campaign_negative_keyword(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->get_campaign_negative_keyword: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing campaign negative keyword. |

### Return type

[**CampaignNegativeKeyword**](CampaignNegativeKeyword.md)

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

# **get_campaign_negative_keyword_ex**
> CampaignNegativeKeywordEx get_campaign_negative_keyword_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)

Gets a campaign negative keyword that has extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaign_negative_keywords_api
from amazon_ads_sponsored_products_client.model.campaign_negative_keyword_ex import CampaignNegativeKeywordEx
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
    api_instance = campaign_negative_keywords_api.CampaignNegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    keyword_id = 3.14 # float | The identifier of an existing campaign negative keyword.

    # example passing only required values which don't have defaults set
    try:
        # Gets a campaign negative keyword that has extended data fields.
        api_response = api_instance.get_campaign_negative_keyword_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, keyword_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->get_campaign_negative_keyword_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **keyword_id** | **float**| The identifier of an existing campaign negative keyword. |

### Return type

[**CampaignNegativeKeywordEx**](CampaignNegativeKeywordEx.md)

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

# **list_campaign_negative_keywords**
> [CampaignNegativeKeyword] list_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of campaign negative keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaign_negative_keywords_api
from amazon_ads_sponsored_products_client.model.campaign_negative_keyword import CampaignNegativeKeyword
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
    api_instance = campaign_negative_keywords_api.CampaignNegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    match_type_filter = "negativePhrase" # str | Restricts results to negative keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. (optional)
    keyword_text = "keywordText_example" # str | Restricts results to negative keywords that match the specified text. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)
    keyword_id_filter = "keywordIdFilter_example" # str | Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of campaign negative keywords.
        api_response = api_instance.list_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->list_campaign_negative_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of campaign negative keywords.
        api_response = api_instance.list_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, match_type_filter=match_type_filter, keyword_text=keyword_text, campaign_id_filter=campaign_id_filter, keyword_id_filter=keyword_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->list_campaign_negative_keywords: %s\n" % e)
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
 **campaign_id_filter** | **str**| Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]
 **keyword_id_filter** | **str**| Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]

### Return type

[**[CampaignNegativeKeyword]**](CampaignNegativeKeyword.md)

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

# **list_campaign_negative_keywords_ex**
> [CampaignNegativeKeywordEx] list_campaign_negative_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of campaign negative keywords that have extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaign_negative_keywords_api
from amazon_ads_sponsored_products_client.model.campaign_negative_keyword_ex import CampaignNegativeKeywordEx
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
    api_instance = campaign_negative_keywords_api.CampaignNegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    match_type_filter = "negativePhrase" # str | Restricts results to negative keywords with match types within the specified comma-separated list. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Ads support center. (optional)
    keyword_text = "keywordText_example" # str | Restricts results to negative keywords that match the specified text. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)
    keyword_id_filter = "keywordIdFilter_example" # str | Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of campaign negative keywords that have extended data fields.
        api_response = api_instance.list_campaign_negative_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->list_campaign_negative_keywords_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of campaign negative keywords that have extended data fields.
        api_response = api_instance.list_campaign_negative_keywords_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, match_type_filter=match_type_filter, keyword_text=keyword_text, campaign_id_filter=campaign_id_filter, keyword_id_filter=keyword_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->list_campaign_negative_keywords_ex: %s\n" % e)
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
 **campaign_id_filter** | **str**| Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]
 **keyword_id_filter** | **str**| Restricts results to negative keywords associated with campaigns specified by identifier in the comma-delimited list. | [optional]

### Return type

[**[CampaignNegativeKeywordEx]**](CampaignNegativeKeywordEx.md)

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

# **update_campaign_negative_keywords**
> [CampaignNegativeKeywordResponse] update_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Updates one or more campaign negative keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaign_negative_keywords_api
from amazon_ads_sponsored_products_client.model.update_campaign_negative_keyword import UpdateCampaignNegativeKeyword
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.campaign_negative_keyword_response import CampaignNegativeKeywordResponse
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
    api_instance = campaign_negative_keywords_api.CampaignNegativeKeywordsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_campaign_negative_keyword = [
        UpdateCampaignNegativeKeyword(None),
    ] # [UpdateCampaignNegativeKeyword] | An array of campaign negative keywords with updated values. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates one or more campaign negative keywords.
        api_response = api_instance.update_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->update_campaign_negative_keywords: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates one or more campaign negative keywords.
        api_response = api_instance.update_campaign_negative_keywords(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_campaign_negative_keyword=update_campaign_negative_keyword)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignNegativeKeywordsApi->update_campaign_negative_keywords: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **update_campaign_negative_keyword** | [**[UpdateCampaignNegativeKeyword]**](UpdateCampaignNegativeKeyword.md)| An array of campaign negative keywords with updated values. | [optional]

### Return type

[**[CampaignNegativeKeywordResponse]**](CampaignNegativeKeywordResponse.md)

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

