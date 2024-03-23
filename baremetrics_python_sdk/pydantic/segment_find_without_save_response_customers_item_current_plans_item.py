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

from baremetrics_python_sdk.pydantic.segment_find_without_save_response_customers_item_current_plans_item_amounts import SegmentFindWithoutSaveResponseCustomersItemCurrentPlansItemAmounts

class SegmentFindWithoutSaveResponseCustomersItemCurrentPlansItem(BaseModel):
    oid: typing.Optional[str] = Field(None, alias='oid')

    source_id: typing.Optional[str] = Field(None, alias='source_id')

    source: typing.Optional[str] = Field(None, alias='source')

    name: typing.Optional[str] = Field(None, alias='name')

    interval: typing.Optional[str] = Field(None, alias='interval')

    interval_count: typing.Optional[int] = Field(None, alias='interval_count')

    trial_duration: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='trial_duration')

    trial_duration_unit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='trial_duration_unit')

    created: typing.Optional[int] = Field(None, alias='created')

    active: typing.Optional[bool] = Field(None, alias='active')

    setup_fees: typing.Optional[int] = Field(None, alias='setup_fees')

    amounts: typing.Optional[SegmentFindWithoutSaveResponseCustomersItemCurrentPlansItemAmounts] = Field(None, alias='amounts')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
