# TargetingClauseEx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **float** | The target identifier. | [optional] 
**campaign_id** | **float** | The identifier of the campaign to which this target is associated. | [optional] 
**ad_group_id** | **float** | The identifier of the ad group to which this target is associated. | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**expression** | [**[TargetingExpressionPredicate]**](TargetingExpressionPredicate.md) | The targeting expression. | [optional] 
**resolved_expression** | [**[TargetingExpressionPredicate]**](TargetingExpressionPredicate.md) | The resolved targeting expression. | [optional] 
**expression_type** | [**ExpressionType**](ExpressionType.md) |  | [optional] 
**bid** | [**Bid**](Bid.md) |  | [optional] 
**creation_date** | **float** | The epoch time that the targeting clause was created. | [optional] 
**last_updated_date** | **float** | The epoch time that the targeting clause was updated. | [optional] 
**serving_status** | **str** | The computed status of the targeting clause. See the [developer notes](https://advertising.amazon.com/API/docs/en-us/get-started/developer-notes) for more information. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


