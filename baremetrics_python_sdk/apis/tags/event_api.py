# coding: utf-8

"""
    Production

    Baremetrics provides real-time subscription metrics for teams built with Stripe, Shopify Partners, Braintree, Recurly, Chargebee, Google Play, and App Store Connect.   In addition to metrics, Baremetrics provides tools that help you reduce churn and grow your business faster:   Recover: Prevent failed charges and keep your hard-earned revenue with our 100% automated toolkit.   Cancellation insights: Learn exactly why your customers cancel, calculate lost revenue by cancellation reason, and send automated emails to win customers back.  Flightpath: Plan for the future with flexible financial modeling tools built for growing SaaS companies.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from baremetrics_python_sdk.paths.v1_cancellation_insights_events.post import CreateInsightEvent
from baremetrics_python_sdk.paths.v1_cancellation_insights_events_id.get import GetEventById
from baremetrics_python_sdk.paths.v1_cancellation_insights_events.get import ListCancellationInsightEvents
from baremetrics_python_sdk.paths.v1_cancellation_insights_events_id.put import UpdateEventById
from baremetrics_python_sdk.apis.tags.event_api_raw import EventApiRaw


class EventApi(
    CreateInsightEvent,
    GetEventById,
    ListCancellationInsightEvents,
    UpdateEventById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EventApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EventApiRaw(api_client)
