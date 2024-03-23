# coding: utf-8

"""
    Production

    Baremetrics provides real-time subscription metrics for teams built with Stripe, Shopify Partners, Braintree, Recurly, Chargebee, Google Play, and App Store Connect.   In addition to metrics, Baremetrics provides tools that help you reduce churn and grow your business faster:   Recover: Prevent failed charges and keep your hard-earned revenue with our 100% automated toolkit.   Cancellation insights: Learn exactly why your customers cancel, calculate lost revenue by cancellation reason, and send automated emails to win customers back.  Flightpath: Plan for the future with flexible financial modeling tools built for growing SaaS companies.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from baremetrics_python_sdk.type.event_create_insight_event_response_event import EventCreateInsightEventResponseEvent

class RequiredEventCreateInsightEventResponse(TypedDict):
    pass

class OptionalEventCreateInsightEventResponse(TypedDict, total=False):
    event: EventCreateInsightEventResponseEvent

class EventCreateInsightEventResponse(RequiredEventCreateInsightEventResponse, OptionalEventCreateInsightEventResponse):
    pass
