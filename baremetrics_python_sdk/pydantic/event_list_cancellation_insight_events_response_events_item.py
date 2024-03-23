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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from baremetrics_python_sdk.pydantic.event_list_cancellation_insight_events_response_events_item_customer import EventListCancellationInsightEventsResponseEventsItemCustomer
from baremetrics_python_sdk.pydantic.event_list_cancellation_insight_events_response_events_item_reason import EventListCancellationInsightEventsResponseEventsItemReason
from baremetrics_python_sdk.pydantic.event_list_cancellation_insight_events_response_events_item_subscriptions import EventListCancellationInsightEventsResponseEventsItemSubscriptions

class EventListCancellationInsightEventsResponseEventsItem(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='comment')

    created_at: typing.Optional[int] = Field(None, alias='created_at')

    subscriptions: typing.Optional[EventListCancellationInsightEventsResponseEventsItemSubscriptions] = Field(None, alias='subscriptions')

    reason: typing.Optional[EventListCancellationInsightEventsResponseEventsItemReason] = Field(None, alias='reason')

    customer: typing.Optional[EventListCancellationInsightEventsResponseEventsItemCustomer] = Field(None, alias='customer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
