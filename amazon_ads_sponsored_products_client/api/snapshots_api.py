"""
    Amazon Ads API - Sponsored Products

    Use the Amazon Ads API for Sponsored Products for campaign, ad group, keyword, negative keyword, and product ad management operations. For more information about Sponsored Products, see the [Sponsored Products Support Center](https://advertising.amazon.com/help?entityId=ENTITY3CWETCZD9HEG2#GWGFKPEWVWG2CLUJ). For onboarding information, see the [account setup](setting-up/account-setup) topic.<br/><br/>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from amazon_ads_sponsored_products_client.api_client import ApiClient, Endpoint as _Endpoint
from amazon_ads_sponsored_products_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.snapshot_request import SnapshotRequest
from amazon_ads_sponsored_products_client.model.snapshot_response import SnapshotResponse


class SnapshotsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_snapshot_status_endpoint = _Endpoint(
            settings={
                'response_type': (SnapshotResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v2/sp/snapshots/{snapshotId}',
                'operation_id': 'get_snapshot_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'amazon_advertising_api_client_id',
                    'amazon_advertising_api_scope',
                    'snapshot_id',
                ],
                'required': [
                    'amazon_advertising_api_client_id',
                    'amazon_advertising_api_scope',
                    'snapshot_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'amazon_advertising_api_client_id':
                        (str,),
                    'amazon_advertising_api_scope':
                        (str,),
                    'snapshot_id':
                        (float,),
                },
                'attribute_map': {
                    'amazon_advertising_api_client_id': 'Amazon-Advertising-API-ClientId',
                    'amazon_advertising_api_scope': 'Amazon-Advertising-API-Scope',
                    'snapshot_id': 'snapshotId',
                },
                'location_map': {
                    'amazon_advertising_api_client_id': 'header',
                    'amazon_advertising_api_scope': 'header',
                    'snapshot_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.request_snapshot_endpoint = _Endpoint(
            settings={
                'response_type': (SnapshotResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v2/sp/{recordType}/snapshot',
                'operation_id': 'request_snapshot',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'amazon_advertising_api_client_id',
                    'amazon_advertising_api_scope',
                    'record_type',
                    'snapshot_request',
                ],
                'required': [
                    'amazon_advertising_api_client_id',
                    'amazon_advertising_api_scope',
                    'record_type',
                    'snapshot_request',
                ],
                'nullable': [
                ],
                'enum': [
                    'record_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('record_type',): {

                        "CAMPAIGNS": "campaigns",
                        "ADGROUPS": "adGroups",
                        "KEYWORDS": "keywords",
                        "NEGATIVEKEYWORDS": "negativeKeywords",
                        "CAMPAIGNNEGATIVEKEYWORDS": "campaignNegativeKeywords",
                        "PRODUCTADS": "productAds",
                        "TARGETS": "targets",
                        "NEGATIVETARGETS": "negativeTargets"
                    },
                },
                'openapi_types': {
                    'amazon_advertising_api_client_id':
                        (str,),
                    'amazon_advertising_api_scope':
                        (str,),
                    'record_type':
                        (str,),
                    'snapshot_request':
                        (SnapshotRequest,),
                },
                'attribute_map': {
                    'amazon_advertising_api_client_id': 'Amazon-Advertising-API-ClientId',
                    'amazon_advertising_api_scope': 'Amazon-Advertising-API-Scope',
                    'record_type': 'recordType',
                },
                'location_map': {
                    'amazon_advertising_api_client_id': 'header',
                    'amazon_advertising_api_scope': 'header',
                    'record_type': 'path',
                    'snapshot_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_snapshot_status(
        self,
        amazon_advertising_api_client_id,
        amazon_advertising_api_scope,
        snapshot_id,
        **kwargs
    ):
        """Gets the status of a requested snapshot.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_snapshot_status(amazon_advertising_api_client_id, amazon_advertising_api_scope, snapshot_id, async_req=True)
        >>> result = thread.get()

        Args:
            amazon_advertising_api_client_id (str): The identifier of a client associated with a \"Login with Amazon\" developer account.
            amazon_advertising_api_scope (str): The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
            snapshot_id (float): The snapshot identifier.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SnapshotResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['amazon_advertising_api_client_id'] = \
            amazon_advertising_api_client_id
        kwargs['amazon_advertising_api_scope'] = \
            amazon_advertising_api_scope
        kwargs['snapshot_id'] = \
            snapshot_id
        return self.get_snapshot_status_endpoint.call_with_http_info(**kwargs)

    def request_snapshot(
        self,
        amazon_advertising_api_client_id,
        amazon_advertising_api_scope,
        record_type,
        snapshot_request,
        **kwargs
    ):
        """Request a file-based snapshot of all entities of the specified type.  # noqa: E501

        Request a file-based snapshot of all entities of the specified type in the account satisfying the filtering criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.request_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type, snapshot_request, async_req=True)
        >>> result = thread.get()

        Args:
            amazon_advertising_api_client_id (str): The identifier of a client associated with a \"Login with Amazon\" developer account.
            amazon_advertising_api_scope (str): The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
            record_type (str): The type of entity for which the snapshot is generated.
            snapshot_request (SnapshotRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SnapshotResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['amazon_advertising_api_client_id'] = \
            amazon_advertising_api_client_id
        kwargs['amazon_advertising_api_scope'] = \
            amazon_advertising_api_scope
        kwargs['record_type'] = \
            record_type
        kwargs['snapshot_request'] = \
            snapshot_request
        return self.request_snapshot_endpoint.call_with_http_info(**kwargs)

