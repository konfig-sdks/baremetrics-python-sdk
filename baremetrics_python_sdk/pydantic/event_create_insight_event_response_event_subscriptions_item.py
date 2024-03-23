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


class EventCreateInsightEventResponseEventSubscriptionsItem(BaseModel):
    oid: typing.Optional[str] = Field(None, alias='oid')

    source_id: typing.Optional[str] = Field(None, alias='source_id')

    source: typing.Optional[str] = Field(None, alias='source')

    canceled_at: typing.Optional[int] = Field(None, alias='canceled_at')

    started_at: typing.Optional[int] = Field(None, alias='started_at')

    processed: typing.Optional[bool] = Field(None, alias='processed')

    active: typing.Optional[bool] = Field(None, alias='active')

    quantity: typing.Optional[int] = Field(None, alias='quantity')

    discount: typing.Optional[int] = Field(None, alias='discount')

    mrr: typing.Optional[int] = Field(None, alias='mrr')

    add_on_mrr: typing.Optional[int] = Field(None, alias='add_on_mrr')

    plan: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='plan')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
