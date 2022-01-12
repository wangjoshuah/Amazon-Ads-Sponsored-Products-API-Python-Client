
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.ad_groups_api import AdGroupsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from amazon_ads_sponsored_products_client.api.ad_groups_api import AdGroupsApi
from amazon_ads_sponsored_products_client.api.bid_recommendations_api import BidRecommendationsApi
from amazon_ads_sponsored_products_client.api.campaign_negative_keywords_api import CampaignNegativeKeywordsApi
from amazon_ads_sponsored_products_client.api.campaigns_api import CampaignsApi
from amazon_ads_sponsored_products_client.api.keywords_api import KeywordsApi
from amazon_ads_sponsored_products_client.api.negative_keywords_api import NegativeKeywordsApi
from amazon_ads_sponsored_products_client.api.negative_product_targeting_api import NegativeProductTargetingApi
from amazon_ads_sponsored_products_client.api.product_ads_api import ProductAdsApi
from amazon_ads_sponsored_products_client.api.product_targeting_api import ProductTargetingApi
from amazon_ads_sponsored_products_client.api.reports_api import ReportsApi
from amazon_ads_sponsored_products_client.api.snapshots_api import SnapshotsApi
from amazon_ads_sponsored_products_client.api.suggested_keywords_api import SuggestedKeywordsApi
