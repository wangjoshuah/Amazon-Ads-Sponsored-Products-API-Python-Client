# amazon_ads_sponsored_products_client.CampaignsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_campaign**](CampaignsApi.md#archive_campaign) | **DELETE** /v2/sp/campaigns/{campaignId} | Archives a campaign.
[**create_campaigns**](CampaignsApi.md#create_campaigns) | **POST** /v2/sp/campaigns | Creates one or more campaigns.
[**get_campaign**](CampaignsApi.md#get_campaign) | **GET** /v2/sp/campaigns/{campaignId} | Gets a campaign specified by identifier.
[**get_campaign_ex**](CampaignsApi.md#get_campaign_ex) | **GET** /v2/sp/campaigns/extended/{campaignId} | Gets a campaign with extended data fields.
[**list_campaigns**](CampaignsApi.md#list_campaigns) | **GET** /v2/sp/campaigns | Gets an array of campaigns.
[**list_campaigns_ex**](CampaignsApi.md#list_campaigns_ex) | **GET** /v2/sp/campaigns/extended | Gets an array of campaigns with extended data fields.
[**update_campaigns**](CampaignsApi.md#update_campaigns) | **PUT** /v2/sp/campaigns | Updates one or more campaigns.


# **archive_campaign**
> CampaignResponse archive_campaign(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)

Archives a campaign.

Sets the campaign status to `archived`. Archived entities cannot be made active again. See [developer notes](https://advertising.amazon.com/API/docs/en-us/get-started/developer-notes#Archiving) for more information.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaigns_api
from amazon_ads_sponsored_products_client.model.campaign_response import CampaignResponse
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    campaign_id = 3.14 # float | The identifier of an existing campaign.

    # example passing only required values which don't have defaults set
    try:
        # Archives a campaign.
        api_response = api_instance.archive_campaign(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->archive_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **campaign_id** | **float**| The identifier of an existing campaign. |

### Return type

[**CampaignResponse**](CampaignResponse.md)

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

# **create_campaigns**
> [CampaignResponse] create_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Creates one or more campaigns.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaigns_api
from amazon_ads_sponsored_products_client.model.create_campaign import CreateCampaign
from amazon_ads_sponsored_products_client.model.campaign_response import CampaignResponse
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_campaign = [
        CreateCampaign(None),
    ] # [CreateCampaign] | An array of campaigns. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates one or more campaigns.
        api_response = api_instance.create_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->create_campaigns: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates one or more campaigns.
        api_response = api_instance.create_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_campaign=create_campaign)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->create_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **create_campaign** | [**[CreateCampaign]**](CreateCampaign.md)| An array of campaigns. | [optional]

### Return type

[**[CampaignResponse]**](CampaignResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Success. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign**
> Campaign get_campaign(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)

Gets a campaign specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaigns_api
from amazon_ads_sponsored_products_client.model.campaign import Campaign
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    campaign_id = 3.14 # float | The identifier of an existing campaign.

    # example passing only required values which don't have defaults set
    try:
        # Gets a campaign specified by identifier.
        api_response = api_instance.get_campaign(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->get_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **campaign_id** | **float**| The identifier of an existing campaign. |

### Return type

[**Campaign**](Campaign.md)

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

# **get_campaign_ex**
> CampaignEx get_campaign_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)

Gets a campaign with extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaigns_api
from amazon_ads_sponsored_products_client.model.campaign_ex import CampaignEx
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    campaign_id = 3.14 # float | The identifier of an existing campaign.

    # example passing only required values which don't have defaults set
    try:
        # Gets a campaign with extended data fields.
        api_response = api_instance.get_campaign_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->get_campaign_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **campaign_id** | **float**| The identifier of an existing campaign. |

### Return type

[**CampaignEx**](CampaignEx.md)

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

# **list_campaigns**
> [Campaign] list_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets an array of campaigns.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaigns_api
from amazon_ads_sponsored_products_client.model.campaign import Campaign
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    name = "name_example" # str | Restricts results to campaigns with the specified name. (optional)
    portfolio_id_filter = "portfolioIdFilter_example" # str | A comma-delimited list of portfolio identifiers. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets an array of campaigns.
        api_response = api_instance.list_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->list_campaigns: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets an array of campaigns.
        api_response = api_instance.list_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, name=name, portfolio_id_filter=portfolio_id_filter, campaign_id_filter=campaign_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->list_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **state_filter** | **str**| Restricts results to resources with state within the specified comma-separated list. | [optional]
 **name** | **str**| Restricts results to campaigns with the specified name. | [optional]
 **portfolio_id_filter** | **str**| A comma-delimited list of portfolio identifiers. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]

### Return type

[**[Campaign]**](Campaign.md)

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

# **list_campaigns_ex**
> [CampaignEx] list_campaigns_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets an array of campaigns with extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaigns_api
from amazon_ads_sponsored_products_client.model.campaign_ex import CampaignEx
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    name = "name_example" # str | Restricts results to campaigns with the specified name. (optional)
    portfolio_id_filter = "portfolioIdFilter_example" # str | A comma-delimited list of portfolio identifiers. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets an array of campaigns with extended data fields.
        api_response = api_instance.list_campaigns_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->list_campaigns_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets an array of campaigns with extended data fields.
        api_response = api_instance.list_campaigns_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, name=name, portfolio_id_filter=portfolio_id_filter, campaign_id_filter=campaign_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->list_campaigns_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **state_filter** | **str**| Restricts results to resources with state within the specified comma-separated list. | [optional]
 **name** | **str**| Restricts results to campaigns with the specified name. | [optional]
 **portfolio_id_filter** | **str**| A comma-delimited list of portfolio identifiers. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]

### Return type

[**[CampaignEx]**](CampaignEx.md)

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

# **update_campaigns**
> [CampaignResponse] update_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Updates one or more campaigns.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import campaigns_api
from amazon_ads_sponsored_products_client.model.campaign_response import CampaignResponse
from amazon_ads_sponsored_products_client.model.update_campaign import UpdateCampaign
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
    api_instance = campaigns_api.CampaignsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_campaign = [
        UpdateCampaign(None),
    ] # [UpdateCampaign] | An array of campaigns with updated values. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates one or more campaigns.
        api_response = api_instance.update_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->update_campaigns: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates one or more campaigns.
        api_response = api_instance.update_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_campaign=update_campaign)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling CampaignsApi->update_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **update_campaign** | [**[UpdateCampaign]**](UpdateCampaign.md)| An array of campaigns with updated values. | [optional]

### Return type

[**[CampaignResponse]**](CampaignResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. An array of campaign response objects reflecting the same order as the request. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

