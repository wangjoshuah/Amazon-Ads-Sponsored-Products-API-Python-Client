# UpdateCampaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **float** | The identifier of an existing campaign to update. | [optional] 
**portfolio_id** | **float** | The identifier of an existing portfolio to which the campaign is associated. | [optional] 
**name** | **str** | The name of the campaign. | [optional] 
**tags** | [**CampaignTags**](CampaignTags.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**daily_budget** | **float** | The daily budget of the campaign. | [optional] 
**start_date** | **str** | The starting date of the campaign. The format of the date is YYYYMMDD. | [optional] 
**end_date** | **str, none_type** | The ending date of the campaign to stop running. The format of the date is YYYYMMDD. | [optional] 
**premium_bid_adjustment** | **bool** | If set to true, Amazon increases the default bid for ads that are eligible to appear in this placement. See developer notes for more information. | [optional] 
**bidding** | [**Bidding**](Bidding.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


