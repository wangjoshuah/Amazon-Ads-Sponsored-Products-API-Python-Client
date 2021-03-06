# amazon-ads-sponsored-products-client
Use the Amazon Ads API for Sponsored Products for campaign, ad group, keyword, negative keyword, and product ad management operations. For more information about Sponsored Products, see the [Sponsored Products Support Center](https://advertising.amazon.com/help?entityId=ENTITY3CWETCZD9HEG2#GWGFKPEWVWG2CLUJ). For onboarding information, see the [account setup](setting-up/account-setup) topic.<br/><br/>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 0.0.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://amzn-clicks.atlassian.net/servicedesk/customer/portals](https://amzn-clicks.atlassian.net/servicedesk/customer/portals)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import amazon_ads_sponsored_products_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import amazon_ads_sponsored_products_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import amazon_ads_sponsored_products_client
from pprint import pprint
from amazon_ads_sponsored_products_client.api import ad_groups_api
from amazon_ads_sponsored_products_client.model.ad_group import AdGroup
from amazon_ads_sponsored_products_client.model.ad_group_ex import AdGroupEx
from amazon_ads_sponsored_products_client.model.ad_group_response import AdGroupResponse
from amazon_ads_sponsored_products_client.model.create_ad_group import CreateAdGroup
from amazon_ads_sponsored_products_client.model.error import Error
from amazon_ads_sponsored_products_client.model.update_ad_group import UpdateAdGroup
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

    try:
        # Archives an ad group.
        api_response = api_instance.archive_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        pprint(api_response)
    except amazon_ads_sponsored_products_client.ApiException as e:
        print("Exception when calling AdGroupsApi->archive_ad_group: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://advertising-api-test.amazon.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdGroupsApi* | [**archive_ad_group**](docs/AdGroupsApi.md#archive_ad_group) | **DELETE** /v2/sp/adGroups/{adGroupId} | Archives an ad group.
*AdGroupsApi* | [**create_ad_groups**](docs/AdGroupsApi.md#create_ad_groups) | **POST** /v2/sp/adGroups | Creates one or more ad groups.
*AdGroupsApi* | [**get_ad_group**](docs/AdGroupsApi.md#get_ad_group) | **GET** /v2/sp/adGroups/{adGroupId} | Gets an ad group specified by identifier.
*AdGroupsApi* | [**get_ad_group_ex**](docs/AdGroupsApi.md#get_ad_group_ex) | **GET** /v2/sp/adGroups/extended/{adGroupId} | Gets an ad group that has extended data fields.
*AdGroupsApi* | [**get_ad_groups**](docs/AdGroupsApi.md#get_ad_groups) | **GET** /v2/sp/adGroups | Gets one or more ad groups.
*AdGroupsApi* | [**get_ad_groups_ex**](docs/AdGroupsApi.md#get_ad_groups_ex) | **GET** /v2/sp/adGroups/extended | Gets ad groups that have extended data fields.
*AdGroupsApi* | [**update_ad_groups**](docs/AdGroupsApi.md#update_ad_groups) | **PUT** /v2/sp/adGroups | Updates one or more ad groups.
*BidRecommendationsApi* | [**create_keyword_bid_recommendations**](docs/BidRecommendationsApi.md#create_keyword_bid_recommendations) | **POST** /v2/sp/keywords/bidRecommendations | Gets bid recommendations for keywords.
*BidRecommendationsApi* | [**get_ad_group_bid_recommendations**](docs/BidRecommendationsApi.md#get_ad_group_bid_recommendations) | **GET** /v2/sp/adGroups/{adGroupId}/bidRecommendations | Gets a bid recommendation for an ad group.
*BidRecommendationsApi* | [**get_bid_recommendations**](docs/BidRecommendationsApi.md#get_bid_recommendations) | **POST** /v2/sp/targets/bidRecommendations | Gets a list of bid recommendations for keyword, product, or auto targeting expressions.
*BidRecommendationsApi* | [**get_keyword_bid_recommendations**](docs/BidRecommendationsApi.md#get_keyword_bid_recommendations) | **GET** /v2/sp/keywords/{keywordId}/bidRecommendations | Gets a bid recommendation for a keyword.
*CampaignNegativeKeywordsApi* | [**archive_campaign_negative_keyword**](docs/CampaignNegativeKeywordsApi.md#archive_campaign_negative_keyword) | **DELETE** /v2/sp/campaignNegativeKeywords/{keywordId} | Archives a campaign negative keyword.
*CampaignNegativeKeywordsApi* | [**create_campaign_negative_keywords**](docs/CampaignNegativeKeywordsApi.md#create_campaign_negative_keywords) | **POST** /v2/sp/campaignNegativeKeywords | Creates one or more campaign negative keywords.
*CampaignNegativeKeywordsApi* | [**get_campaign_negative_keyword**](docs/CampaignNegativeKeywordsApi.md#get_campaign_negative_keyword) | **GET** /v2/sp/campaignNegativeKeywords/{keywordId} | Gets a campaign negative keyword specified by identifier.
*CampaignNegativeKeywordsApi* | [**get_campaign_negative_keyword_ex**](docs/CampaignNegativeKeywordsApi.md#get_campaign_negative_keyword_ex) | **GET** /v2/sp/campaignNegativeKeywords/extended/{keywordId} | Gets a campaign negative keyword that has extended data fields.
*CampaignNegativeKeywordsApi* | [**list_campaign_negative_keywords**](docs/CampaignNegativeKeywordsApi.md#list_campaign_negative_keywords) | **GET** /v2/sp/campaignNegativeKeywords | Gets a list of campaign negative keywords.
*CampaignNegativeKeywordsApi* | [**list_campaign_negative_keywords_ex**](docs/CampaignNegativeKeywordsApi.md#list_campaign_negative_keywords_ex) | **GET** /v2/sp/campaignNegativeKeywords/extended | Gets a list of campaign negative keywords that have extended data fields.
*CampaignNegativeKeywordsApi* | [**update_campaign_negative_keywords**](docs/CampaignNegativeKeywordsApi.md#update_campaign_negative_keywords) | **PUT** /v2/sp/campaignNegativeKeywords | Updates one or more campaign negative keywords.
*CampaignsApi* | [**archive_campaign**](docs/CampaignsApi.md#archive_campaign) | **DELETE** /v2/sp/campaigns/{campaignId} | Archives a campaign.
*CampaignsApi* | [**create_campaigns**](docs/CampaignsApi.md#create_campaigns) | **POST** /v2/sp/campaigns | Creates one or more campaigns.
*CampaignsApi* | [**get_campaign**](docs/CampaignsApi.md#get_campaign) | **GET** /v2/sp/campaigns/{campaignId} | Gets a campaign specified by identifier.
*CampaignsApi* | [**get_campaign_ex**](docs/CampaignsApi.md#get_campaign_ex) | **GET** /v2/sp/campaigns/extended/{campaignId} | Gets a campaign with extended data fields.
*CampaignsApi* | [**list_campaigns**](docs/CampaignsApi.md#list_campaigns) | **GET** /v2/sp/campaigns | Gets an array of campaigns.
*CampaignsApi* | [**list_campaigns_ex**](docs/CampaignsApi.md#list_campaigns_ex) | **GET** /v2/sp/campaigns/extended | Gets an array of campaigns with extended data fields.
*CampaignsApi* | [**update_campaigns**](docs/CampaignsApi.md#update_campaigns) | **PUT** /v2/sp/campaigns | Updates one or more campaigns.
*KeywordsApi* | [**archive_keyword**](docs/KeywordsApi.md#archive_keyword) | **DELETE** /v2/sp/keywords/{keywordId} | Archives a keyword.
*KeywordsApi* | [**create_keywords**](docs/KeywordsApi.md#create_keywords) | **POST** /v2/sp/keywords | Creates one or more keywords.
*KeywordsApi* | [**get_keyword**](docs/KeywordsApi.md#get_keyword) | **GET** /v2/sp/keywords/{keywordId} | Gets a keyword specified by identifier.
*KeywordsApi* | [**get_keyword_ex**](docs/KeywordsApi.md#get_keyword_ex) | **GET** /v2/sp/keywords/extended/{keywordId} | Gets a keyword with extended data fields.
*KeywordsApi* | [**list_keywords**](docs/KeywordsApi.md#list_keywords) | **GET** /v2/sp/keywords | 
*KeywordsApi* | [**list_keywords_ex**](docs/KeywordsApi.md#list_keywords_ex) | **GET** /v2/sp/keywords/extended | Gets a list of keywords that have extended data fields.
*KeywordsApi* | [**update_keywords**](docs/KeywordsApi.md#update_keywords) | **PUT** /v2/sp/keywords | Updates one or more keywords.
*NegativeKeywordsApi* | [**archive_negative_keyword**](docs/NegativeKeywordsApi.md#archive_negative_keyword) | **DELETE** /v2/sp/negativeKeywords/{keywordId} | Archives a negative keyword.
*NegativeKeywordsApi* | [**create_negative_keywords**](docs/NegativeKeywordsApi.md#create_negative_keywords) | **POST** /v2/sp/negativeKeywords | Creates one or more negative keywords.
*NegativeKeywordsApi* | [**get_negative_keyword**](docs/NegativeKeywordsApi.md#get_negative_keyword) | **GET** /v2/sp/negativeKeywords/{keywordId} | Gets a negative keyword specified by identifier.
*NegativeKeywordsApi* | [**get_negative_keyword_ex**](docs/NegativeKeywordsApi.md#get_negative_keyword_ex) | **GET** /v2/sp/negativeKeywords/extended/{keywordId} | Gets a negative keyword that has extended data fields.
*NegativeKeywordsApi* | [**list_negative_keywords**](docs/NegativeKeywordsApi.md#list_negative_keywords) | **GET** /v2/sp/negativeKeywords | Gets a list of negative keyword objects.
*NegativeKeywordsApi* | [**list_negative_keywords_ex**](docs/NegativeKeywordsApi.md#list_negative_keywords_ex) | **GET** /v2/sp/negativeKeywords/extended | Gets a list of negative keywords that have extended data fields.
*NegativeKeywordsApi* | [**update_negative_keywords**](docs/NegativeKeywordsApi.md#update_negative_keywords) | **PUT** /v2/sp/negativeKeywords | Updates one or more negative keywords.
*NegativeProductTargetingApi* | [**archive_negative_targeting_clause**](docs/NegativeProductTargetingApi.md#archive_negative_targeting_clause) | **DELETE** /v2/sp/negativeTargets/{targetId} | Archives a negative targeting clause.
*NegativeProductTargetingApi* | [**create_negative_targeting_clauses**](docs/NegativeProductTargetingApi.md#create_negative_targeting_clauses) | **POST** /v2/sp/negativeTargets | Creates one ore more negative targeting expressions.
*NegativeProductTargetingApi* | [**get_negative_targeting_clause**](docs/NegativeProductTargetingApi.md#get_negative_targeting_clause) | **GET** /v2/sp/negativeTargets/{targetId} | Get a negative targeting clause specified by identifier.
*NegativeProductTargetingApi* | [**get_negative_targeting_clause_ex**](docs/NegativeProductTargetingApi.md#get_negative_targeting_clause_ex) | **GET** /v2/sp/negativeTargets/extended/{targetId} | Get a negative targeting clause specified by identifier.
*NegativeProductTargetingApi* | [**list_negative_targeting_clauses**](docs/NegativeProductTargetingApi.md#list_negative_targeting_clauses) | **GET** /v2/sp/negativeTargets | Gets a list of negative targeting clauses filtered by specified criteria.
*NegativeProductTargetingApi* | [**list_negative_targeting_clauses_ex**](docs/NegativeProductTargetingApi.md#list_negative_targeting_clauses_ex) | **GET** /v2/sp/negativeTargets/extended | Gets a list of negative targeting clauses filtered by specified criteria.
*NegativeProductTargetingApi* | [**update_negative_targeting_clause**](docs/NegativeProductTargetingApi.md#update_negative_targeting_clause) | **PUT** /v2/sp/negativeTargets | Updates one or more negative targeting clauses.
*ProductAdsApi* | [**archive_product_ad**](docs/ProductAdsApi.md#archive_product_ad) | **DELETE** /v2/sp/productAds/{adId} | Archives a product ad.
*ProductAdsApi* | [**create_product_ads**](docs/ProductAdsApi.md#create_product_ads) | **POST** /v2/sp/productAds | Creates one or more product ads.
*ProductAdsApi* | [**get_product_ad**](docs/ProductAdsApi.md#get_product_ad) | **GET** /v2/sp/productAds/{adId} | Gets a product ad specified by identifier.
*ProductAdsApi* | [**get_product_ad_ex**](docs/ProductAdsApi.md#get_product_ad_ex) | **GET** /v2/sp/productAds/extended/{adId} | Gets extended data for a product ad specified by identifier.
*ProductAdsApi* | [**list_product_ads**](docs/ProductAdsApi.md#list_product_ads) | **GET** /v2/sp/productAds | Gets a list of product ads filtered by specified criteria.
*ProductAdsApi* | [**list_product_ads_ex**](docs/ProductAdsApi.md#list_product_ads_ex) | **GET** /v2/sp/productAds/extended | Gets extended data for a list of product ads filtered by specified criteria.
*ProductAdsApi* | [**update_product_ads**](docs/ProductAdsApi.md#update_product_ads) | **PUT** /v2/sp/productAds | Updates one or more product ads specified by identifier.
*ProductTargetingApi* | [**archive_targeting_clause**](docs/ProductTargetingApi.md#archive_targeting_clause) | **DELETE** /v2/sp/targets/{targetId} | Archives a targeting clause.
*ProductTargetingApi* | [**create_target_recommendations**](docs/ProductTargetingApi.md#create_target_recommendations) | **POST** /v2/sp/targets/productRecommendations | Gets a list of recommended products for targeting.
*ProductTargetingApi* | [**create_targeting_clauses**](docs/ProductTargetingApi.md#create_targeting_clauses) | **POST** /v2/sp/targets | Creates one or more targeting expressions.
*ProductTargetingApi* | [**get_brand_recommendations**](docs/ProductTargetingApi.md#get_brand_recommendations) | **GET** /v2/sp/targets/brands | Get recommended brands for Sponsored Products.
*ProductTargetingApi* | [**get_targeting_clause**](docs/ProductTargetingApi.md#get_targeting_clause) | **GET** /v2/sp/targets/{targetId} | Get a targeting clause specified by identifier.
*ProductTargetingApi* | [**get_targeting_clause_ex**](docs/ProductTargetingApi.md#get_targeting_clause_ex) | **GET** /v2/sp/targets/extended/{targetId} | Get a targeting clause specified by identifier.
*ProductTargetingApi* | [**list_targeting_clauses**](docs/ProductTargetingApi.md#list_targeting_clauses) | **GET** /v2/sp/targets | Gets a list of targeting clauses filtered by specified criteria.
*ProductTargetingApi* | [**list_targeting_clauses_ex**](docs/ProductTargetingApi.md#list_targeting_clauses_ex) | **GET** /v2/sp/targets/extended | Gets a list of targeting clauses filtered by specified criteria.
*ProductTargetingApi* | [**update_targeting_clause**](docs/ProductTargetingApi.md#update_targeting_clause) | **PUT** /v2/sp/targets | Updates one or more targeting clauses.
*ReportsApi* | [**download_report**](docs/ReportsApi.md#download_report) | **GET** /v2/reports/{reportId}/download | Downloads a previously requested report identified by report ID.
*ReportsApi* | [**get_report**](docs/ReportsApi.md#get_report) | **GET** /v2/reports/{reportId} | Gets a previously requested report specified by identifier.
*ReportsApi* | [**request_report**](docs/ReportsApi.md#request_report) | **POST** /v2/sp/{recordType}/report | Requests a Sponsored Products report.
*SnapshotsApi* | [**get_snapshot_status**](docs/SnapshotsApi.md#get_snapshot_status) | **GET** /v2/sp/snapshots/{snapshotId} | Gets the status of a requested snapshot.
*SnapshotsApi* | [**request_snapshot**](docs/SnapshotsApi.md#request_snapshot) | **POST** /v2/sp/{recordType}/snapshot | Request a file-based snapshot of all entities of the specified type.
*SuggestedKeywordsApi* | [**bulk_get_asin_suggested_keywords**](docs/SuggestedKeywordsApi.md#bulk_get_asin_suggested_keywords) | **POST** /v2/sp/asins/suggested/keywords | Gets suggested keyword for a specified list of ASINs.
*SuggestedKeywordsApi* | [**get_ad_group_suggested_keywords**](docs/SuggestedKeywordsApi.md#get_ad_group_suggested_keywords) | **GET** /v2/sp/adGroups/{adGroupId}/suggested/keywords | Gets suggested keywords for the specified ad group.
*SuggestedKeywordsApi* | [**get_ad_group_suggested_keywords_ex**](docs/SuggestedKeywordsApi.md#get_ad_group_suggested_keywords_ex) | **GET** /v2/sp/adGroups/{adGroupId}/suggested/keywords/extended | Gets suggested keywords with extended data for the specified ad group.
*SuggestedKeywordsApi* | [**get_asin_suggested_keywords**](docs/SuggestedKeywordsApi.md#get_asin_suggested_keywords) | **GET** /v2/sp/asins/{asinValue}/suggested/keywords | Gets suggested keywords for the specified ASIN.


## Documentation For Models

 - [AdGroup](docs/AdGroup.md)
 - [AdGroupBidRecommendationsResponse](docs/AdGroupBidRecommendationsResponse.md)
 - [AdGroupEx](docs/AdGroupEx.md)
 - [AdGroupResponse](docs/AdGroupResponse.md)
 - [AdGroupSuggestedKeywordsResponse](docs/AdGroupSuggestedKeywordsResponse.md)
 - [AdGroupSuggestedKeywordsResponseEx](docs/AdGroupSuggestedKeywordsResponseEx.md)
 - [Bid](docs/Bid.md)
 - [BidRecommendationRequest](docs/BidRecommendationRequest.md)
 - [BidRecommendationsForTargetsResponse](docs/BidRecommendationsForTargetsResponse.md)
 - [BidRecommendationsForTargetsResponseRecommendations](docs/BidRecommendationsForTargetsResponseRecommendations.md)
 - [BidRecommendationsResponse](docs/BidRecommendationsResponse.md)
 - [Bidding](docs/Bidding.md)
 - [BiddingAdjustments](docs/BiddingAdjustments.md)
 - [BrandResponse](docs/BrandResponse.md)
 - [BulkGetAsinSuggestedKeywordsResponse](docs/BulkGetAsinSuggestedKeywordsResponse.md)
 - [Campaign](docs/Campaign.md)
 - [CampaignEx](docs/CampaignEx.md)
 - [CampaignNegativeKeyword](docs/CampaignNegativeKeyword.md)
 - [CampaignNegativeKeywordEx](docs/CampaignNegativeKeywordEx.md)
 - [CampaignNegativeKeywordResponse](docs/CampaignNegativeKeywordResponse.md)
 - [CampaignResponse](docs/CampaignResponse.md)
 - [CampaignTags](docs/CampaignTags.md)
 - [CategoryResponse](docs/CategoryResponse.md)
 - [CreateAdGroup](docs/CreateAdGroup.md)
 - [CreateCampaign](docs/CreateCampaign.md)
 - [CreateCampaignNegativeKeyword](docs/CreateCampaignNegativeKeyword.md)
 - [CreateKeyword](docs/CreateKeyword.md)
 - [CreateNegativeKeyword](docs/CreateNegativeKeyword.md)
 - [CreateNegativeTargetingClause](docs/CreateNegativeTargetingClause.md)
 - [CreateProductAd](docs/CreateProductAd.md)
 - [CreateTargetingClause](docs/CreateTargetingClause.md)
 - [Error](docs/Error.md)
 - [ExpressionType](docs/ExpressionType.md)
 - [GetAsinSuggestedKeywordsResponse](docs/GetAsinSuggestedKeywordsResponse.md)
 - [GetAsinSuggestedKeywordsResponseSuggestedKeywords](docs/GetAsinSuggestedKeywordsResponseSuggestedKeywords.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse200Recommendations](docs/InlineResponse200Recommendations.md)
 - [Keyword](docs/Keyword.md)
 - [KeywordBidRecommendationsData](docs/KeywordBidRecommendationsData.md)
 - [KeywordBidRecommendationsDataKeywords](docs/KeywordBidRecommendationsDataKeywords.md)
 - [KeywordBidRecommendationsResponse](docs/KeywordBidRecommendationsResponse.md)
 - [KeywordEx](docs/KeywordEx.md)
 - [KeywordResponse](docs/KeywordResponse.md)
 - [MatchType](docs/MatchType.md)
 - [NegativeKeyword](docs/NegativeKeyword.md)
 - [NegativeKeywordEx](docs/NegativeKeywordEx.md)
 - [NegativeKeywordResponse](docs/NegativeKeywordResponse.md)
 - [NegativeMatchType](docs/NegativeMatchType.md)
 - [NegativeTargetingClause](docs/NegativeTargetingClause.md)
 - [NegativeTargetingClauseEx](docs/NegativeTargetingClauseEx.md)
 - [NegativeTargetingClauseResponse](docs/NegativeTargetingClauseResponse.md)
 - [ProductAd](docs/ProductAd.md)
 - [ProductAdEx](docs/ProductAdEx.md)
 - [ProductAdExServingStatusDetails](docs/ProductAdExServingStatusDetails.md)
 - [ProductAdResponse](docs/ProductAdResponse.md)
 - [ProductRecommendationsResponse](docs/ProductRecommendationsResponse.md)
 - [ProductRecommendationsResponseRecommendedProducts](docs/ProductRecommendationsResponseRecommendedProducts.md)
 - [RefinementsResponse](docs/RefinementsResponse.md)
 - [RefinementsResponseBrands](docs/RefinementsResponseBrands.md)
 - [Report](docs/Report.md)
 - [SnapshotRequest](docs/SnapshotRequest.md)
 - [SnapshotResponse](docs/SnapshotResponse.md)
 - [State](docs/State.md)
 - [SuggestedBid](docs/SuggestedBid.md)
 - [TargetingClause](docs/TargetingClause.md)
 - [TargetingClauseEx](docs/TargetingClauseEx.md)
 - [TargetingClauseResponse](docs/TargetingClauseResponse.md)
 - [TargetingExpression](docs/TargetingExpression.md)
 - [TargetingExpressionExpressions](docs/TargetingExpressionExpressions.md)
 - [TargetingExpressionPredicate](docs/TargetingExpressionPredicate.md)
 - [UpdateAdGroup](docs/UpdateAdGroup.md)
 - [UpdateCampaign](docs/UpdateCampaign.md)
 - [UpdateCampaignNegativeKeyword](docs/UpdateCampaignNegativeKeyword.md)
 - [UpdateKeyword](docs/UpdateKeyword.md)
 - [UpdateNegativeKeyword](docs/UpdateNegativeKeyword.md)
 - [UpdateNegativeTargetingClause](docs/UpdateNegativeTargetingClause.md)
 - [UpdateProductAd](docs/UpdateProductAd.md)
 - [UpdateTargetingClause](docs/UpdateTargetingClause.md)


## Documentation For Authorization


## bearer

- **Type**: Bearer authentication


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in amazon_ads_sponsored_products_client.apis and amazon_ads_sponsored_products_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from amazon_ads_sponsored_products_client.api.default_api import DefaultApi`
- `from amazon_ads_sponsored_products_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.apis import *
from amazon_ads_sponsored_products_client.models import *
```

