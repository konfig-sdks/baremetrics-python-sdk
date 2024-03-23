# coding: utf-8

"""
    Production

    Baremetrics provides real-time subscription metrics for teams built with Stripe, Shopify Partners, Braintree, Recurly, Chargebee, Google Play, and App Store Connect.   In addition to metrics, Baremetrics provides tools that help you reduce churn and grow your business faster:   Recover: Prevent failed charges and keep your hard-earned revenue with our 100% automated toolkit.   Cancellation insights: Learn exactly why your customers cancel, calculate lost revenue by cancellation reason, and send automated emails to win customers back.  Flightpath: Plan for the future with flexible financial modeling tools built for growing SaaS companies.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from baremetrics_python_sdk.paths.v1_segments.post import CreateRequestRaw
from baremetrics_python_sdk.paths.v1_segments_search.post import FindWithoutSaveRaw
from baremetrics_python_sdk.paths.v1_segments_fields.get import GetFieldsRaw
from baremetrics_python_sdk.paths.v1_segments.get import ListSegmentsRaw
from baremetrics_python_sdk.paths.v1_segments_id.delete import RemoveByIdRaw
from baremetrics_python_sdk.paths.v1_segments_id.get import ShowDetailsRaw
from baremetrics_python_sdk.paths.v1_segments_id.put import UpdateByIdRaw


class SegmentApiRaw(
    CreateRequestRaw,
    FindWithoutSaveRaw,
    GetFieldsRaw,
    ListSegmentsRaw,
    RemoveByIdRaw,
    ShowDetailsRaw,
    UpdateByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
