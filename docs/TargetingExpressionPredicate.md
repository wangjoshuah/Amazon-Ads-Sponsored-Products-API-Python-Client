# TargetingExpressionPredicate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The expression value | [optional] 
**type** | **str** | The type of targeting expression. You can specify values for the following predicates: | Predicate | Description | | --- | --- | | &#x60;queryBroadMatches&#x60; |  | &#x60;asinCategorySameAs&#x60; | Negatively Target the same category as the category expressed. | | &#x60;asinBrandSameAs&#x60; | Target the brand that is the same as the brand expressed. | | &#x60;asinPriceLessThan&#x60; | Target a price that is less than the price expressed. | | &#x60;asinPriceBetween&#x60; | Target a price that is between the prices expressed. | | &#x60;asinPriceGreaterThan&#x60; | Target a price that is greater than the price expressed. | | &#x60;asinReviewRatingLessThan&#x60; | Target a review rating less than the review rating that is expressed. | | &#x60;asinReviewRatingBetween&#x60; | Target a review rating that is between the review ratings expressed. | | &#x60;asinReviewRatingGreaterThan&#x60; | Target a review rating that is greater than the review rating expressed. | | &#x60;asinSameAs&#x60; | Target an ASIN that is the same as the ASIN expressed. | | &#x60;asinIsPrimeShippingEligible&#x60; | Target products that are Prime Shipping Eligible. This refinement can be applied at a category or brand level only. | | &#x60;asinAgeRangeSameAs&#x60; | Target an age range that is in the expressed range. This refinement can be applied for toys and games categories only. | | &#x60;asinGenreSameAs&#x60; | Target products related to the expressed genre. This refinement can be applied for Books and eBooks categories only.   | | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


