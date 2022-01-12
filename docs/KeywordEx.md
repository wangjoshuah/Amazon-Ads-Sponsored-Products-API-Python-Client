# KeywordEx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_id** | **float** | The identifier of the keyword. | [optional] 
**campaign_id** | **float** | The identifer of the campaign to which the keyword is associated. | [optional] 
**ad_group_id** | **float** | The identifier of the ad group to which this keyword is associated. | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**keyword_text** | **str** | The text of the expression to match against a search query. | [optional] 
**native_language_keyword** | **str** | The unlocalized keyword text in the preferred locale of the advertiser. | [optional] 
**match_type** | [**MatchType**](MatchType.md) |  | [optional] 
**bid** | **float** | Bid associated with this keyword. This table details the maximum allowable bid (in local currency) for keywords by marketplace: | Marketplace | Currency | Min / Max bid for SP | | --- | --- | --- | | US | USD | 0.02 / 1000 | | CA | CAD | 0.02 / 1000 | | UK | GBP | 0.02 / 1000 | | DE | EUR | 0.02 / 1000 | | FR | EUR | 0.02 / 1000 | | ES | EUR | 0.02 / 1000 | | IT | EUR | 0.02 / 1000 | | JP | JPY | 2.0 / 100000 | | AU | AUD | 0.10 / 1410 | | AE | AED | 0.24 / 184.0 | | [optional] 
**creation_date** | **float** | Creation date in epoch time. | [optional] 
**last_updated_date** | **float** | Date of last update in epoch time. | [optional] 
**serving_status** | **str** | The serving status of the keyword. See the **computed status** section of the [developer notes](https://advertising.amazon.com/API/docs/en-us/get-started/developer-notes) for definitions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


