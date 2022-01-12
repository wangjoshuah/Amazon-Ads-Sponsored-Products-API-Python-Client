# amazon_ads_sponsored_products_client.AdGroupsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_ad_group**](AdGroupsApi.md#archive_ad_group) | **DELETE** /v2/sp/adGroups/{adGroupId} | Archives an ad group.
[**create_ad_groups**](AdGroupsApi.md#create_ad_groups) | **POST** /v2/sp/adGroups | Creates one or more ad groups.
[**get_ad_group**](AdGroupsApi.md#get_ad_group) | **GET** /v2/sp/adGroups/{adGroupId} | Gets an ad group specified by identifier.
[**get_ad_group_ex**](AdGroupsApi.md#get_ad_group_ex) | **GET** /v2/sp/adGroups/extended/{adGroupId} | Gets an ad group that has extended data fields.
[**get_ad_groups**](AdGroupsApi.md#get_ad_groups) | **GET** /v2/sp/adGroups | Gets one or more ad groups.
[**get_ad_groups_ex**](AdGroupsApi.md#get_ad_groups_ex) | **GET** /v2/sp/adGroups/extended | Gets ad groups that have extended data fields.
[**update_ad_groups**](AdGroupsApi.md#update_ad_groups) | **PUT** /v2/sp/adGroups | Updates one or more ad groups.


# **archive_ad_group**
> AdGroupResponse archive_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Archives an ad group.

Sets the ad group status to `archived`. Archived entities cannot be made active again. See developer notes for more information.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import ad_groups_api
from amazon_ads_sponsored_products_client.model.ad_group_response import AdGroupResponse
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 3.14 # float | The identifier of an existing ad group.

    # example passing only required values which don't have defaults set
    try:
        # Archives an ad group.
        api_response = api_instance.archive_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->archive_ad_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_group_id** | **float**| The identifier of an existing ad group. |

### Return type

[**AdGroupResponse**](AdGroupResponse.md)

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

# **create_ad_groups**
> [AdGroupResponse] create_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Creates one or more ad groups.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import ad_groups_api
from amazon_ads_sponsored_products_client.model.ad_group_response import AdGroupResponse
from amazon_ads_sponsored_products_client.model.create_ad_group import CreateAdGroup
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_ad_group = [
        CreateAdGroup(None),
    ] # [CreateAdGroup] | An array of ad groups. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates one or more ad groups.
        api_response = api_instance.create_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->create_ad_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates one or more ad groups.
        api_response = api_instance.create_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_ad_group=create_ad_group)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->create_ad_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **create_ad_group** | [**[CreateAdGroup]**](CreateAdGroup.md)| An array of ad groups. | [optional]

### Return type

[**[AdGroupResponse]**](AdGroupResponse.md)

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

# **get_ad_group**
> AdGroup get_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Gets an ad group specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import ad_groups_api
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.ad_group import AdGroup
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 3.14 # float | The identifier of an existing ad group.

    # example passing only required values which don't have defaults set
    try:
        # Gets an ad group specified by identifier.
        api_response = api_instance.get_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->get_ad_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_group_id** | **float**| The identifier of an existing ad group. |

### Return type

[**AdGroup**](AdGroup.md)

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

# **get_ad_group_ex**
> AdGroupEx get_ad_group_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Gets an ad group that has extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import ad_groups_api
from amazon_ads_sponsored_products_client.model.ad_group_ex import AdGroupEx
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 3.14 # float | The identifier of an existing ad group.

    # example passing only required values which don't have defaults set
    try:
        # Gets an ad group that has extended data fields.
        api_response = api_instance.get_ad_group_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->get_ad_group_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_group_id** | **float**| The identifier of an existing ad group. |

### Return type

[**AdGroupEx**](AdGroupEx.md)

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

# **get_ad_groups**
> [AdGroup] get_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets one or more ad groups.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import ad_groups_api
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.ad_group import AdGroup
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    campaign_type = "campaignType_example" # str | Restricts results to ad groups within campaign types specified in comma-separated list. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    name = "name_example" # str | Restricts results to campaigns with the specified name. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets one or more ad groups.
        api_response = api_instance.get_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->get_ad_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets one or more ad groups.
        api_response = api_instance.get_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, campaign_type=campaign_type, state_filter=state_filter, name=name, campaign_id_filter=campaign_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->get_ad_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **campaign_type** | **str**| Restricts results to ad groups within campaign types specified in comma-separated list. | [optional]
 **state_filter** | **str**| Restricts results to resources with state within the specified comma-separated list. | [optional]
 **name** | **str**| Restricts results to campaigns with the specified name. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]

### Return type

[**[AdGroup]**](AdGroup.md)

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

# **get_ad_groups_ex**
> [AdGroupEx] get_ad_groups_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets ad groups that have extended data fields.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import ad_groups_api
from amazon_ads_sponsored_products_client.model.ad_group_ex import AdGroupEx
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    campaign_type = "campaignType_example" # str | Restricts results to ad groups within campaign types specified in comma-separated list. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    name = "name_example" # str | Restricts results to campaigns with the specified name. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets ad groups that have extended data fields.
        api_response = api_instance.get_ad_groups_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->get_ad_groups_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets ad groups that have extended data fields.
        api_response = api_instance.get_ad_groups_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, campaign_type=campaign_type, state_filter=state_filter, name=name, campaign_id_filter=campaign_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->get_ad_groups_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **start_index** | **float**| 0-indexed record offset for the result set. | [optional] if omitted the server will use the default value of 0
 **count** | **float**| Number of records to include in the paged response. Defaults to max page size. | [optional]
 **campaign_type** | **str**| Restricts results to ad groups within campaign types specified in comma-separated list. | [optional]
 **state_filter** | **str**| Restricts results to resources with state within the specified comma-separated list. | [optional]
 **name** | **str**| Restricts results to campaigns with the specified name. | [optional]
 **campaign_id_filter** | **str**| A comma-delimited list of campaign identifiers. | [optional]

### Return type

[**[AdGroupEx]**](AdGroupEx.md)

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

# **update_ad_groups**
> [AdGroupResponse] update_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Updates one or more ad groups.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import ad_groups_api
from amazon_ads_sponsored_products_client.model.ad_group_response import AdGroupResponse
from amazon_ads_sponsored_products_client.model.update_ad_group import UpdateAdGroup
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_ad_group = [
        UpdateAdGroup(None),
    ] # [UpdateAdGroup] | An array of ad groups that have updated field values. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates one or more ad groups.
        api_response = api_instance.update_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->update_ad_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates one or more ad groups.
        api_response = api_instance.update_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_ad_group=update_ad_group)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->update_ad_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **update_ad_group** | [**[UpdateAdGroup]**](UpdateAdGroup.md)| An array of ad groups that have updated field values. | [optional]

### Return type

[**[AdGroupResponse]**](AdGroupResponse.md)

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

