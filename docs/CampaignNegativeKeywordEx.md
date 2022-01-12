# CampaignNegativeKeywordEx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_id** | **float** | The identifier of the campaign negative keyword. | [optional] 
**campaign_id** | **float** | The identifer of the campaign to which the campaign negative keyword is associated. | [optional] 
**state** | **str** | The campaign negative keyword state. | [optional]  if omitted the server will use the default value of "enabled"
**keyword_text** | **str** | The text of the expression to match against a search query. | [optional] 
**match_type** | [**NegativeMatchType**](NegativeMatchType.md) |  | [optional] 
**creation_date** | **float** | Creation date in epoch time. | [optional] 
**last_updated_date** | **float** | Date of last update in epoch time. | [optional] 
**serving_status** | **str** | The serving status of the campaign negative keyword. See the **computed status** section of the [developer notes](https://advertising.amazon.com/API/docs/en-us/get-started/developer-notes) for definitions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


