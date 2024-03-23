# coding: utf-8

"""
    Production

    Baremetrics provides real-time subscription metrics for teams built with Stripe, Shopify Partners, Braintree, Recurly, Chargebee, Google Play, and App Store Connect.   In addition to metrics, Baremetrics provides tools that help you reduce churn and grow your business faster:   Recover: Prevent failed charges and keep your hard-earned revenue with our 100% automated toolkit.   Cancellation insights: Learn exactly why your customers cancel, calculate lost revenue by cancellation reason, and send automated emails to win customers back.  Flightpath: Plan for the future with flexible financial modeling tools built for growing SaaS companies.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from baremetrics_python_sdk import schemas  # noqa: F401


class MetricShowCohortsResponseItemCells(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['MetricShowCohortsResponseItemCellsItem']:
            return MetricShowCohortsResponseItemCellsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MetricShowCohortsResponseItemCellsItem'], typing.List['MetricShowCohortsResponseItemCellsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MetricShowCohortsResponseItemCells':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MetricShowCohortsResponseItemCellsItem':
        return super().__getitem__(i)

from baremetrics_python_sdk.model.metric_show_cohorts_response_item_cells_item import MetricShowCohortsResponseItemCellsItem
