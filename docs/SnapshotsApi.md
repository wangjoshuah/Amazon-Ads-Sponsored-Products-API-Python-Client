# amazon_ads_sponsored_products_client.SnapshotsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snapshot_status**](SnapshotsApi.md#get_snapshot_status) | **GET** /v2/sp/snapshots/{snapshotId} | Gets the status of a requested snapshot.
[**request_snapshot**](SnapshotsApi.md#request_snapshot) | **POST** /v2/sp/{recordType}/snapshot | Request a file-based snapshot of all entities of the specified type.


# **get_snapshot_status**
> SnapshotResponse get_snapshot_status(amazon_advertising_api_client_id, amazon_advertising_api_scope, snapshot_id)

Gets the status of a requested snapshot.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import snapshots_api
from amazon_ads_sponsored_products_client.model.snapshot_response import SnapshotResponse
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
    api_instance = snapshots_api.SnapshotsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    snapshot_id = 3.14 # float | The snapshot identifier.

    # example passing only required values which don't have defaults set
    try:
        # Gets the status of a requested snapshot.
        api_response = api_instance.get_snapshot_status(amazon_advertising_api_client_id, amazon_advertising_api_scope, snapshot_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SnapshotsApi->get_snapshot_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **snapshot_id** | **float**| The snapshot identifier. |

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**307** | Temporary redirect. |  * Location -  <br>  |
**401** | Unauthorized. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_snapshot**
> SnapshotResponse request_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type, snapshot_request)

Request a file-based snapshot of all entities of the specified type.

Request a file-based snapshot of all entities of the specified type in the account satisfying the filtering criteria.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import snapshots_api
from amazon_ads_sponsored_products_client.model.snapshot_response import SnapshotResponse
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.snapshot_request import SnapshotRequest
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
    api_instance = snapshots_api.SnapshotsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    record_type = "campaigns" # str | The type of entity for which the snapshot is generated.
    snapshot_request = SnapshotRequest(None) # SnapshotRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Request a file-based snapshot of all entities of the specified type.
        api_response = api_instance.request_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type, snapshot_request)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling SnapshotsApi->request_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **record_type** | **str**| The type of entity for which the snapshot is generated. |
 **snapshot_request** | [**SnapshotRequest**](SnapshotRequest.md)|  |

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

