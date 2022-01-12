# amazon_ads_sponsored_products_client.ReportsApi

All URIs are relative to *https://advertising-api-test.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_report**](ReportsApi.md#download_report) | **GET** /v2/reports/{reportId}/download | Downloads a previously requested report identified by report ID.
[**get_report**](ReportsApi.md#get_report) | **GET** /v2/reports/{reportId} | Gets a previously requested report specified by identifier.
[**request_report**](ReportsApi.md#request_report) | **POST** /v2/sp/{recordType}/report | Requests a Sponsored Products report.


# **download_report**
> file_type download_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, report_id)

Downloads a previously requested report identified by report ID.

Gets a `307 Temporary Redirect` response that includes a `location` header with the value set to an AWS S3 path where the report is located. The path expires after 30 seconds. If the path expires before the report is downloaded, a new report request must be created.  The report file contains one row per entity for which performance data is present. These records are represented as JSON containing the ID attribute corresponding to the `recordType`, the segment (if specified), and each of the metrics in the request.  **Note**: The report files in S3 are gzipped.  *Example report download*  ``` $ curl -o /tmp/report.json.gz \"https://sandboxreports.s3.amazonaws.com/amzn1.clicksAPI.v1.m1.xxxxxxx.xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx?AWSAccessKeyId=XXXXXXXXXXXXXXX&amp;Expires=1476479900&amp;Signature=xxxxxxxxxxxxxxxxxxxx\" ```

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    report_id = "reportId_example" # str | The identifier of the requested report.

    # example passing only required values which don't have defaults set
    try:
        # Downloads a previously requested report identified by report ID.
        api_response = api_instance.download_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, report_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ReportsApi->download_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **report_id** | **str**| The identifier of the requested report. |

### Return type

**file_type**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**307** | Successful operation. |  * Location - Redirect URI with S3 file location containing report data <br>  |
**400** | Bad request. |  -  |
**404** | Not found - requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too many requests - request was rate-limited. Retry later. |  -  |
**500** | Internal server error - something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> InlineResponse2002 get_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, report_id)

Gets a previously requested report specified by identifier.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import reports_api
from amazon_ads_sponsored_products_client.model.inline_response2002 import InlineResponse2002
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
    api_instance = reports_api.ReportsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    report_id = "reportId_example" # str | The report identifier.

    # example passing only required values which don't have defaults set
    try:
        # Gets a previously requested report specified by identifier.
        api_response = api_instance.get_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, report_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ReportsApi->get_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **report_id** | **str**| The report identifier. |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **request_report**
> InlineResponse2001 request_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type)

Requests a Sponsored Products report.

Request the creation of a performance report for all entities of a single type which have performance data to report. Record types can be one of `campaigns`, `adGroups`, `keywords`, `productAds`, `asins`, and `targets`. **Note** that for `asin` reports, the report currently can **not** include metrics associated with both keywords and targets. If the `targetingId` value is set in the request, the report filters on targets and does not return sales associated with keywords. If the `targetingId` value is **not** set in the request, the report filters on keywords and does not return sales associated with targets. Therefore, the default behavior filters the report on keywords. Also note that if both `keywordId` **and** `targetingId` values are passed, the report filters on targets only and does **not** return keywords.

### Example

* Bearer Authentication (bearer):

```python
import time
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api import reports_api
from amazon_ads_sponsored_products_client.model.report import Report
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.inline_response2001 import InlineResponse2001
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
    api_instance = reports_api.ReportsApi(api_client)
    amazon_advertising_api_client_id = "Amazon-Advertising-API-ClientId_example" # str | The identifier of a client associated with a \"Login with Amazon\" developer account.
    amazon_advertising_api_scope = "Amazon-Advertising-API-Scope_example" # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    record_type = "campaigns" # str | The type of entity for which the report should be generated.
    report = Report(None) # Report |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Requests a Sponsored Products report.
        api_response = api_instance.request_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ReportsApi->request_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Requests a Sponsored Products report.
        api_response = api_instance.request_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type, report=report)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling ReportsApi->request_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; developer account. |
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. |
 **record_type** | **str**| The type of entity for which the report should be generated. |
 **report** | [**Report**](Report.md)|  | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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
**406** | One or more values specified for a parameter was not within the specified acceptable range. |  -  |
**422** | An invalid parameter was specified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

