"""
    Amazon Ads API - Sponsored Products

    Use the Amazon Ads API for Sponsored Products for campaign, ad group, keyword, negative keyword, and product ad management operations. For more information about Sponsored Products, see the [Sponsored Products Support Center](https://advertising.amazon.com/help?entityId=ENTITY3CWETCZD9HEG2#GWGFKPEWVWG2CLUJ). For onboarding information, see the [account setup](setting-up/account-setup) topic.<br/><br/>   # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.api.product_targeting_api import ProductTargetingApi  # noqa: E501


class TestProductTargetingApi(unittest.TestCase):
    """ProductTargetingApi unit test stubs"""

    def setUp(self):
        self.api = ProductTargetingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_targeting_clause(self):
        """Test case for archive_targeting_clause

        Archives a targeting clause.  # noqa: E501
        """
        pass

    def test_create_target_recommendations(self):
        """Test case for create_target_recommendations

        Gets a list of recommended products for targeting.  # noqa: E501
        """
        pass

    def test_create_targeting_clauses(self):
        """Test case for create_targeting_clauses

        Creates one or more targeting expressions.  # noqa: E501
        """
        pass

    def test_get_brand_recommendations(self):
        """Test case for get_brand_recommendations

        Get recommended brands for Sponsored Products.  # noqa: E501
        """
        pass

    def test_get_targeting_clause(self):
        """Test case for get_targeting_clause

        Get a targeting clause specified by identifier.  # noqa: E501
        """
        pass

    def test_get_targeting_clause_ex(self):
        """Test case for get_targeting_clause_ex

        Get a targeting clause specified by identifier.  # noqa: E501
        """
        pass

    def test_list_targeting_clauses(self):
        """Test case for list_targeting_clauses

        Gets a list of targeting clauses filtered by specified criteria.  # noqa: E501
        """
        pass

    def test_list_targeting_clauses_ex(self):
        """Test case for list_targeting_clauses_ex

        Gets a list of targeting clauses filtered by specified criteria.  # noqa: E501
        """
        pass

    def test_update_targeting_clause(self):
        """Test case for update_targeting_clause

        Updates one or more targeting clauses.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
