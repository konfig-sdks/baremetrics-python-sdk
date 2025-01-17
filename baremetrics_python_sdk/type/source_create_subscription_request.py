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

from baremetrics_python_sdk.type.source_create_subscription_request_addons import SourceCreateSubscriptionRequestAddons

class RequiredSourceCreateSubscriptionRequest(TypedDict):
    # Your unique ID for the subscription
    oid: str

    # A unix timestamp of when this subscription started
    started_at: datetime

    # Your unique ID for the plan
    plan_oid: str

    # Your unique ID for the customer
    customer_oid: str

class OptionalSourceCreateSubscriptionRequest(TypedDict, total=False):
    # A unix timestamp of when this subscription was, or should be canceled. This cannot be changed, so only set this if you are certain you know when the subscription will end.
    canceled_at: datetime

    addons: SourceCreateSubscriptionRequestAddons

    quantity: int

    # Integer value (in the same currency as the plan)
    discount: int

class SourceCreateSubscriptionRequest(RequiredSourceCreateSubscriptionRequest, OptionalSourceCreateSubscriptionRequest):
    pass
