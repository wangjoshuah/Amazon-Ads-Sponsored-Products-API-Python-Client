# Bidding

Specifies bidding controls.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** | The bidding strategy. | Value | Strategy name | Description | |----------------|---------------|-------------| | &#x60;legacyForSales&#x60; | Dynamic bids - down only | Lowers your bids in real time when your ad may be less likely to convert to a sale. Campaigns created before the release of the bidding controls feature used this setting by default. | | &#x60;autoForSales&#x60; | Dynamic bids - up and down | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale. | | &#x60;manual&#x60; | Fixed bid | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding. | | [optional] 
**adjustments** | [**[BiddingAdjustments]**](BiddingAdjustments.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


