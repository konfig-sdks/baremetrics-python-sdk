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

from baremetrics_python_sdk.pydantic.source_update_subscription_request_addons import SourceUpdateSubscriptionRequestAddons

class SourceUpdateSubscriptionRequest(BaseModel):
    # Your unique ID for the plan
    plan_oid: str = Field(alias='plan_oid')

    # A unix timestamp of when this change occurred. Defaults to now
    occurred_at: typing.Optional[datetime] = Field(None, alias='occurred_at')

    addons: typing.Optional[SourceUpdateSubscriptionRequestAddons] = Field(None, alias='addons')

    quantity: typing.Optional[int] = Field(None, alias='quantity')

    # Integer value (in the same currency as the plan)
    discount: typing.Optional[int] = Field(None, alias='discount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
