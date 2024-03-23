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


class SourceCreateCustomerRecordRequest(BaseModel):
    # Your unique ID for the customer
    oid: str = Field(alias='oid')

    name: typing.Optional[str] = Field(None, alias='name')

    # Your own notes for this customer. These will be displayed in the profile
    notes: typing.Optional[str] = Field(None, alias='notes')

    # An email address for this customer. This is used to lookup extra profile information
    email: typing.Optional[str] = Field(None, alias='email')

    # A unix timestamp of when this customer was created. Defaults to now.
    created: typing.Optional[datetime] = Field(None, alias='created')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
