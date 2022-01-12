"""
    Amazon Ads API - Sponsored Products

    Use the Amazon Ads API for Sponsored Products for campaign, ad group, keyword, negative keyword, and product ad management operations. For more information about Sponsored Products, see the [Sponsored Products Support Center](https://advertising.amazon.com/help?entityId=ENTITY3CWETCZD9HEG2#GWGFKPEWVWG2CLUJ). For onboarding information, see the [account setup](setting-up/account-setup) topic.<br/><br/>   # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api.negative_keywords_api import NegativeKeywordsApi  # noqa: E501


class TestNegativeKeywordsApi(unittest.TestCase):
    """NegativeKeywordsApi unit test stubs"""

    def setUp(self):
        self.api = NegativeKeywordsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_negative_keyword(self):
        """Test case for archive_negative_keyword

        Archives a negative keyword.  # noqa: E501
        """
        pass

    def test_create_negative_keywords(self):
        """Test case for create_negative_keywords

        Creates one or more negative keywords.  # noqa: E501
        """
        pass

    def test_get_negative_keyword(self):
        """Test case for get_negative_keyword

        Gets a negative keyword specified by identifier.  # noqa: E501
        """
        pass

    def test_get_negative_keyword_ex(self):
        """Test case for get_negative_keyword_ex

        Gets a negative keyword that has extended data fields.  # noqa: E501
        """
        pass

    def test_list_negative_keywords(self):
        """Test case for list_negative_keywords

        Gets a list of negative keyword objects.  # noqa: E501
        """
        pass

    def test_list_negative_keywords_ex(self):
        """Test case for list_negative_keywords_ex

        Gets a list of negative keywords that have extended data fields.  # noqa: E501
        """
        pass

    def test_update_negative_keywords(self):
        """Test case for update_negative_keywords

        Updates one or more negative keywords.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
