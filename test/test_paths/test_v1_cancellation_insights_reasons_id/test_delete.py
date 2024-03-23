# coding: utf-8

"""
    Production

    Baremetrics provides real-time subscription metrics for teams built with Stripe, Shopify Partners, Braintree, Recurly, Chargebee, Google Play, and App Store Connect.   In addition to metrics, Baremetrics provides tools that help you reduce churn and grow your business faster:   Recover: Prevent failed charges and keep your hard-earned revenue with our 100% automated toolkit.   Cancellation insights: Learn exactly why your customers cancel, calculate lost revenue by cancellation reason, and send automated emails to win customers back.  Flightpath: Plan for the future with flexible financial modeling tools built for growing SaaS companies.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import baremetrics_python_sdk
from baremetrics_python_sdk.paths.v1_cancellation_insights_reasons_id import delete
from baremetrics_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1CancellationInsightsReasonsId(ApiTestMixin, unittest.TestCase):
    """
    V1CancellationInsightsReasonsId unit test stubs
        Delete Reason
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 202




if __name__ == '__main__':
    unittest.main()
