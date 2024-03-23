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


class RequiredSourceCreatePlanRequest(TypedDict):
    # Your unique ID for the plan
    oid: str

    # Your internal name for this plan. This will be displayed in the Plan Breakout section
    name: str

    # The ISO code of the currency of this plan. E.G: usd
    currency: str

    # How much is this plan? (In cents)
    amount: int

    # day, month or year
    interval: str

    interval_count: int

class OptionalSourceCreatePlanRequest(TypedDict, total=False):
    # The duration of this trial. This is to be used in conjunction with trial_duration_unit
    trial_duration: int

    # This is to be used in conjunction with trial_duration
    trial_duration_unit: str

class SourceCreatePlanRequest(RequiredSourceCreatePlanRequest, OptionalSourceCreatePlanRequest):
    pass
