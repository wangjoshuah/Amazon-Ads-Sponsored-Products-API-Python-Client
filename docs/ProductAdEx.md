# ProductAdEx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_id** | **float** | The product ad identifier. | [optional] 
**campaign_id** | **float** | The campaign identifier. | [optional] 
**ad_group_id** | **float** | The ad group identifier. | [optional] 
**sku** | **str** | The SKU associated with the product. Defined for seller accounts only. | [optional] 
**asin** | **str** | The ASIN associated with the product. Defined for vendors only. | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**creation_date** | **float** | The epoch date the product ad was created. | [optional] 
**last_updated_date** | **float** | The epoch date the product ad was last updated. | [optional] 
**serving_status** | **str** | The computed status of the product ad. See the [developer notes](https://advertising.amazon.com/API/docs/en-us/get-started/developer-notes) for more information. | [optional] 
**serving_status_details** | [**[ProductAdExServingStatusDetails]**](ProductAdExServingStatusDetails.md) | Details of serving status. Only statuses related to moderation according to the ad policy are currently included. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


