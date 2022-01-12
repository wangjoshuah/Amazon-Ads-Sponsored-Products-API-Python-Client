"""
    Amazon Ads API - Sponsored Products

    Use the Amazon Ads API for Sponsored Products for campaign, ad group, keyword, negative keyword, and product ad management operations. For more information about Sponsored Products, see the [Sponsored Products Support Center](https://advertising.amazon.com/help?entityId=ENTITY3CWETCZD9HEG2#GWGFKPEWVWG2CLUJ). For onboarding information, see the [account setup](setting-up/account-setup) topic.<br/><br/>   # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from amazon_ads_sponsored_products_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from amazon_ads_sponsored_products_client.exceptions import ApiAttributeError


def lazy_import():
    from amazon_ads_sponsored_products_client.model.match_type import MatchType
    from amazon_ads_sponsored_products_client.model.state import State
    globals()['MatchType'] = MatchType
    globals()['State'] = State


class KeywordEx(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('serving_status',): {
            'TARGETING_CLAUSE_ARCHIVED': "TARGETING_CLAUSE_ARCHIVED",
            'TARGETING_CLAUSE_PAUSED': "TARGETING_CLAUSE_PAUSED",
            'TARGETING_CLAUSE_STATUS_LIVE': "TARGETING_CLAUSE_STATUS_LIVE",
            'TARGETING_CLAUSE_POLICING_SUSPENDED': "TARGETING_CLAUSE_POLICING_SUSPENDED",
            'CAMPAIGN_OUT_OF_BUDGET': "CAMPAIGN_OUT_OF_BUDGET",
            'AD_GROUP_PAUSED': "AD_GROUP_PAUSED",
            'AD_GROUP_ARCHIVED': "AD_GROUP_ARCHIVED",
            'CAMPAIGN_PAUSED': "CAMPAIGN_PAUSED",
            'CAMPAIGN_ARCHIVED': "CAMPAIGN_ARCHIVED",
            'ACCOUNT_OUT_OF_BUDGET': "ACCOUNT_OUT_OF_BUDGET",
            'PENDING_START_DATE': "PENDING_START_DATE",
        },
    }

    validations = {
        ('bid',): {
            'inclusive_minimum': 0.02,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'keyword_id': (float,),  # noqa: E501
            'campaign_id': (float,),  # noqa: E501
            'ad_group_id': (float,),  # noqa: E501
            'state': (State,),  # noqa: E501
            'keyword_text': (str,),  # noqa: E501
            'native_language_keyword': (str,),  # noqa: E501
            'match_type': (MatchType,),  # noqa: E501
            'bid': (float,),  # noqa: E501
            'creation_date': (float,),  # noqa: E501
            'last_updated_date': (float,),  # noqa: E501
            'serving_status': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'keyword_id': 'keywordId',  # noqa: E501
        'campaign_id': 'campaignId',  # noqa: E501
        'ad_group_id': 'adGroupId',  # noqa: E501
        'state': 'state',  # noqa: E501
        'keyword_text': 'keywordText',  # noqa: E501
        'native_language_keyword': 'nativeLanguageKeyword',  # noqa: E501
        'match_type': 'matchType',  # noqa: E501
        'bid': 'bid',  # noqa: E501
        'creation_date': 'creationDate',  # noqa: E501
        'last_updated_date': 'lastUpdatedDate',  # noqa: E501
        'serving_status': 'servingStatus',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """KeywordEx - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            keyword_id (float): The identifier of the keyword.. [optional]  # noqa: E501
            campaign_id (float): The identifer of the campaign to which the keyword is associated.. [optional]  # noqa: E501
            ad_group_id (float): The identifier of the ad group to which this keyword is associated.. [optional]  # noqa: E501
            state (State): [optional]  # noqa: E501
            keyword_text (str): The text of the expression to match against a search query.. [optional]  # noqa: E501
            native_language_keyword (str): The unlocalized keyword text in the preferred locale of the advertiser.. [optional]  # noqa: E501
            match_type (MatchType): [optional]  # noqa: E501
            bid (float): Bid associated with this keyword. This table details the maximum allowable bid (in local currency) for keywords by marketplace: | Marketplace | Currency | Min / Max bid for SP | | --- | --- | --- | | US | USD | 0.02 / 1000 | | CA | CAD | 0.02 / 1000 | | UK | GBP | 0.02 / 1000 | | DE | EUR | 0.02 / 1000 | | FR | EUR | 0.02 / 1000 | | ES | EUR | 0.02 / 1000 | | IT | EUR | 0.02 / 1000 | | JP | JPY | 2.0 / 100000 | | AU | AUD | 0.10 / 1410 | | AE | AED | 0.24 / 184.0 |. [optional]  # noqa: E501
            creation_date (float): Creation date in epoch time.. [optional]  # noqa: E501
            last_updated_date (float): Date of last update in epoch time.. [optional]  # noqa: E501
            serving_status (str): The serving status of the keyword. See the **computed status** section of the [developer notes](https://advertising.amazon.com/API/docs/en-us/get-started/developer-notes) for definitions.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """KeywordEx - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            keyword_id (float): The identifier of the keyword.. [optional]  # noqa: E501
            campaign_id (float): The identifer of the campaign to which the keyword is associated.. [optional]  # noqa: E501
            ad_group_id (float): The identifier of the ad group to which this keyword is associated.. [optional]  # noqa: E501
            state (State): [optional]  # noqa: E501
            keyword_text (str): The text of the expression to match against a search query.. [optional]  # noqa: E501
            native_language_keyword (str): The unlocalized keyword text in the preferred locale of the advertiser.. [optional]  # noqa: E501
            match_type (MatchType): [optional]  # noqa: E501
            bid (float): Bid associated with this keyword. This table details the maximum allowable bid (in local currency) for keywords by marketplace: | Marketplace | Currency | Min / Max bid for SP | | --- | --- | --- | | US | USD | 0.02 / 1000 | | CA | CAD | 0.02 / 1000 | | UK | GBP | 0.02 / 1000 | | DE | EUR | 0.02 / 1000 | | FR | EUR | 0.02 / 1000 | | ES | EUR | 0.02 / 1000 | | IT | EUR | 0.02 / 1000 | | JP | JPY | 2.0 / 100000 | | AU | AUD | 0.10 / 1410 | | AE | AED | 0.24 / 184.0 |. [optional]  # noqa: E501
            creation_date (float): Creation date in epoch time.. [optional]  # noqa: E501
            last_updated_date (float): Date of last update in epoch time.. [optional]  # noqa: E501
            serving_status (str): The serving status of the keyword. See the **computed status** section of the [developer notes](https://advertising.amazon.com/API/docs/en-us/get-started/developer-notes) for definitions.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
