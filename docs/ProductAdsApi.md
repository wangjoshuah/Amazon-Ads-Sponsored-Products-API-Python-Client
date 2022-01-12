# amazon_ads_sponsored_products_client.ProductAdsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_product_ad**](ProductAdsApi.md#archive_product_ad) | **DELETE** /v2/sp/productAds/{adId} | Archives a product ad.
[**create_product_ads**](ProductAdsApi.md#create_product_ads) | **POST** /v2/sp/productAds | Creates one or more product ads.
[**get_product_ad**](ProductAdsApi.md#get_product_ad) | **GET** /v2/sp/productAds/{adId} | Gets a product ad specified by identifier.
[**get_product_ad_ex**](ProductAdsApi.md#get_product_ad_ex) | **GET** /v2/sp/productAds/extended/{adId} | Gets extended data for a product ad specified by identifier.
[**list_product_ads**](ProductAdsApi.md#list_product_ads) | **GET** /v2/sp/productAds | Gets a list of product ads filtered by specified criteria.
[**list_product_ads_ex**](ProductAdsApi.md#list_product_ads_ex) | **GET** /v2/sp/productAds/extended | Gets extended data for a list of product ads filtered by specified criteria.
[**update_product_ads**](ProductAdsApi.md#update_product_ads) | **PUT** /v2/sp/productAds | Updates one or more product ads specified by identifier.


# **archive_product_ad**
> ProductAdResponse archive_product_ad(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)

Archives a product ad.

Sets the state of a specified product ad to `archived`. Note that once the state is set to `archived` it cannot be changed.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_ads_api
from amazon_ads_sponsored_products_client.model.product_ad_response import ProductAdResponse
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
    api_instance = product_ads_api.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_id = 3.14 # float | A product ad identifier.

    # example passing only required values which don't have defaults set
    try:
        # Archives a product ad.
        api_response = api_instance.archive_product_ad(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->archive_product_ad: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_id** | **float**| A product ad identifier. |

### Return type

[**ProductAdResponse**](ProductAdResponse.md)

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

# **create_product_ads**
> [ProductAdResponse] create_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Creates one or more product ads.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_ads_api
from amazon_ads_sponsored_products_client.model.product_ad_response import ProductAdResponse
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.create_product_ad import CreateProductAd
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
    api_instance = product_ads_api.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_product_ad = [
        CreateProductAd(None),
    ] # [CreateProductAd] | A list of product ads for creation. Note that the `SKU` field is used by sellers and the `ASIN` field is used by vendors. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates one or more product ads.
        api_response = api_instance.create_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->create_product_ads: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates one or more product ads.
        api_response = api_instance.create_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_product_ad=create_product_ad)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->create_product_ads: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **create_product_ad** | [**[CreateProductAd]**](CreateProductAd.md)| A list of product ads for creation. Note that the &#x60;SKU&#x60; field is used by sellers and the &#x60;ASIN&#x60; field is used by vendors. | [optional]

### Return type

[**[ProductAdResponse]**](ProductAdResponse.md)

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

# **get_product_ad**
> ProductAd get_product_ad(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)

Gets a product ad specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_ads_api
from amazon_ads_sponsored_products_client.model.product_ad import ProductAd
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
    api_instance = product_ads_api.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_id = 3.14 # float | A product ad identifier.

    # example passing only required values which don't have defaults set
    try:
        # Gets a product ad specified by identifier.
        api_response = api_instance.get_product_ad(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->get_product_ad: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_id** | **float**| A product ad identifier. |

### Return type

[**ProductAd**](ProductAd.md)

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

# **get_product_ad_ex**
> ProductAdEx get_product_ad_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)

Gets extended data for a product ad specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_ads_api
from amazon_ads_sponsored_products_client.model.product_ad_ex import ProductAdEx
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
    api_instance = product_ads_api.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_id = 3.14 # float | A product ad identifier.

    # example passing only required values which don't have defaults set
    try:
        # Gets extended data for a product ad specified by identifier.
        api_response = api_instance.get_product_ad_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->get_product_ad_ex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **ad_id** | **float**| A product ad identifier. |

### Return type

[**ProductAdEx**](ProductAdEx.md)

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

# **list_product_ads**
> [ProductAd] list_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets a list of product ads filtered by specified criteria.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_ads_api
from amazon_ads_sponsored_products_client.model.product_ad import ProductAd
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
    api_instance = product_ads_api.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    ad_id_filter = "adIdFilter_example" # str | Restricts results to product ads associated with the product ad identifiers specified in the comma-delimited list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of product ads filtered by specified criteria.
        api_response = api_instance.list_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->list_product_ads: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of product ads filtered by specified criteria.
        api_response = api_instance.list_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, ad_id_filter=ad_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->list_product_ads: %s\n" % e)
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
 **ad_id_filter** | **str**| Restricts results to product ads associated with the product ad identifiers specified in the comma-delimited list. | [optional]

### Return type

[**[ProductAd]**](ProductAd.md)

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

# **list_product_ads_ex**
> [ProductAdEx] list_product_ads_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Gets extended data for a list of product ads filtered by specified criteria.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_ads_api
from amazon_ads_sponsored_products_client.model.product_ad_ex import ProductAdEx
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
    api_instance = product_ads_api.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # float | 0-indexed record offset for the result set. (optional) if omitted the server will use the default value of 0
    count = 3.14 # float | Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = "enabled" # str | Restricts results to resources with state within the specified comma-separated list. (optional)
    campaign_id_filter = "campaignIdFilter_example" # str | A comma-delimited list of campaign identifiers. (optional)
    ad_group_id_filter = "adGroupIdFilter_example" # str | Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list. (optional)
    ad_id_filter = "adIdFilter_example" # str | Restricts results to product ads associated with the product ad identifiers specified in the comma-delimited list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets extended data for a list of product ads filtered by specified criteria.
        api_response = api_instance.list_product_ads_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->list_product_ads_ex: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets extended data for a list of product ads filtered by specified criteria.
        api_response = api_instance.list_product_ads_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, ad_id_filter=ad_id_filter)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->list_product_ads_ex: %s\n" % e)
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
 **ad_id_filter** | **str**| Restricts results to product ads associated with the product ad identifiers specified in the comma-delimited list. | [optional]

### Return type

[**[ProductAdEx]**](ProductAdEx.md)

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

# **update_product_ads**
> [ProductAdResponse] update_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Updates one or more product ads specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import product_ads_api
from amazon_ads_sponsored_products_client.model.product_ad_response import ProductAdResponse
from amazon_ads_sponsored_products_client.model.update_product_ad import UpdateProductAd
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
    api_instance = product_ads_api.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_product_ad = [
        UpdateProductAd(None),
    ] # [UpdateProductAd] | A list of product ad objects with updated values for the `state` field. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates one or more product ads specified by identifier.
        api_response = api_instance.update_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->update_product_ads: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates one or more product ads specified by identifier.
        api_response = api_instance.update_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_product_ad=update_product_ad)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ProductAdsApi->update_product_ads: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **update_product_ad** | [**[UpdateProductAd]**](UpdateProductAd.md)| A list of product ad objects with updated values for the &#x60;state&#x60; field. | [optional]

### Return type

[**[ProductAdResponse]**](ProductAdResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. A list of product ad objects with updated fields, in the same order as the list in the request body. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

