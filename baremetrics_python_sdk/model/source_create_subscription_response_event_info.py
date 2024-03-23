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


class SourceCreateSubscriptionResponseEventInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            oid = schemas.StrSchema
            started_at = schemas.IntSchema
            plan_oid = schemas.StrSchema
            customer_oid = schemas.StrSchema
            canceled_at = schemas.AnyTypeSchema
            quantity = schemas.IntSchema
        
            @staticmethod
            def addons() -> typing.Type['SourceCreateSubscriptionResponseEventInfoAddons']:
                return SourceCreateSubscriptionResponseEventInfoAddons
            __annotations__ = {
                "oid": oid,
                "started_at": started_at,
                "plan_oid": plan_oid,
                "customer_oid": customer_oid,
                "canceled_at": canceled_at,
                "quantity": quantity,
                "addons": addons,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oid"]) -> MetaOapg.properties.oid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["started_at"]) -> MetaOapg.properties.started_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan_oid"]) -> MetaOapg.properties.plan_oid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_oid"]) -> MetaOapg.properties.customer_oid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canceled_at"]) -> MetaOapg.properties.canceled_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addons"]) -> 'SourceCreateSubscriptionResponseEventInfoAddons': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["oid", "started_at", "plan_oid", "customer_oid", "canceled_at", "quantity", "addons", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oid"]) -> typing.Union[MetaOapg.properties.oid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["started_at"]) -> typing.Union[MetaOapg.properties.started_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan_oid"]) -> typing.Union[MetaOapg.properties.plan_oid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_oid"]) -> typing.Union[MetaOapg.properties.customer_oid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canceled_at"]) -> typing.Union[MetaOapg.properties.canceled_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> typing.Union[MetaOapg.properties.quantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addons"]) -> typing.Union['SourceCreateSubscriptionResponseEventInfoAddons', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["oid", "started_at", "plan_oid", "customer_oid", "canceled_at", "quantity", "addons", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        oid: typing.Union[MetaOapg.properties.oid, str, schemas.Unset] = schemas.unset,
        started_at: typing.Union[MetaOapg.properties.started_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        plan_oid: typing.Union[MetaOapg.properties.plan_oid, str, schemas.Unset] = schemas.unset,
        customer_oid: typing.Union[MetaOapg.properties.customer_oid, str, schemas.Unset] = schemas.unset,
        canceled_at: typing.Union[MetaOapg.properties.canceled_at, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        addons: typing.Union['SourceCreateSubscriptionResponseEventInfoAddons', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceCreateSubscriptionResponseEventInfo':
        return super().__new__(
            cls,
            *args,
            oid=oid,
            started_at=started_at,
            plan_oid=plan_oid,
            customer_oid=customer_oid,
            canceled_at=canceled_at,
            quantity=quantity,
            addons=addons,
            _configuration=_configuration,
            **kwargs,
        )

from baremetrics_python_sdk.model.source_create_subscription_response_event_info_addons import SourceCreateSubscriptionResponseEventInfoAddons
