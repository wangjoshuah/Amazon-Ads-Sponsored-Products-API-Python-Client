# CreateCampaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | **float** | The identifier of an existing portfolio to which the campaign is associated. | [optional] 
**name** | **str** | A name for the campaign. | [optional] 
**tags** | [**CampaignTags**](CampaignTags.md) |  | [optional] 
**campaign_type** | **str** | The advertising product managed by this campaign. | [optional]  if omitted the server will use the default value of "sponsoredProducts"
**targeting_type** | **str** | The type of targeting for the campaign. | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**daily_budget** | **float** | A daily budget for the campaign. | [optional] 
**start_date** | **str** | A starting date for the campaign to go live. The format of the date is YYYYMMDD. | [optional] 
**end_date** | **str, none_type** | An ending date for the campaign to stop running. The format of the date is YYYYMMDD. | [optional] 
**premium_bid_adjustment** | **bool** | If set to true, Amazon increases the default bid for ads that are eligible to appear in this placement. See developer notes for more information. | [optional] 
**bidding** | [**Bidding**](Bidding.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


