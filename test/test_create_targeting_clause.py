"""
    Amazon Ads API - Sponsored Products

    Use the Amazon Ads API for Sponsored Products for campaign, ad group, keyword, negative keyword, and product ad management operations. For more information about Sponsored Products, see the [Sponsored Products Support Center](https://advertising.amazon.com/help?entityId=ENTITY3CWETCZD9HEG2#GWGFKPEWVWG2CLUJ). For onboarding information, see the [account setup](setting-up/account-setup) topic.<br/><br/>   # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import amazon_ads_sponsored_products_client
from amazon_ads_sponsored_products_client.model.bid import Bid
from amazon_ads_sponsored_products_client.model.expression_type import ExpressionType
from amazon_ads_sponsored_products_client.model.state import State
from amazon_ads_sponsored_products_client.model.targeting_expression_predicate import TargetingExpressionPredicate
globals()['Bid'] = Bid
globals()['ExpressionType'] = ExpressionType
globals()['State'] = State
globals()['TargetingExpressionPredicate'] = TargetingExpressionPredicate
from amazon_ads_sponsored_products_client.model.create_targeting_clause import CreateTargetingClause


class TestCreateTargetingClause(unittest.TestCase):
    """CreateTargetingClause unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateTargetingClause(self):
        """Test CreateTargetingClause"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateTargetingClause()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
