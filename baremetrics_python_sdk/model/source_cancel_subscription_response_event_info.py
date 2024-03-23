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


class SourceCancelSubscriptionResponseEventInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            canceled_at = schemas.IntSchema
        
            @staticmethod
            def addons() -> typing.Type['SourceCancelSubscriptionResponseEventInfoAddons']:
                return SourceCancelSubscriptionResponseEventInfoAddons
            __annotations__ = {
                "canceled_at": canceled_at,
                "addons": addons,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canceled_at"]) -> MetaOapg.properties.canceled_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addons"]) -> 'SourceCancelSubscriptionResponseEventInfoAddons': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["canceled_at", "addons", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canceled_at"]) -> typing.Union[MetaOapg.properties.canceled_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addons"]) -> typing.Union['SourceCancelSubscriptionResponseEventInfoAddons', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["canceled_at", "addons", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        canceled_at: typing.Union[MetaOapg.properties.canceled_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        addons: typing.Union['SourceCancelSubscriptionResponseEventInfoAddons', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceCancelSubscriptionResponseEventInfo':
        return super().__new__(
            cls,
            *args,
            canceled_at=canceled_at,
            addons=addons,
            _configuration=_configuration,
            **kwargs,
        )

from baremetrics_python_sdk.model.source_cancel_subscription_response_event_info_addons import SourceCancelSubscriptionResponseEventInfoAddons
