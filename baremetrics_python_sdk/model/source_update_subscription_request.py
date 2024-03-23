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


class SourceUpdateSubscriptionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "plan_oid",
        }
        
        class properties:
            plan_oid = schemas.StrSchema
            occurred_at = schemas.DateTimeSchema
        
            @staticmethod
            def addons() -> typing.Type['SourceUpdateSubscriptionRequestAddons']:
                return SourceUpdateSubscriptionRequestAddons
            quantity = schemas.Int32Schema
            discount = schemas.Int32Schema
            __annotations__ = {
                "plan_oid": plan_oid,
                "occurred_at": occurred_at,
                "addons": addons,
                "quantity": quantity,
                "discount": discount,
            }
    
    plan_oid: MetaOapg.properties.plan_oid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan_oid"]) -> MetaOapg.properties.plan_oid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["occurred_at"]) -> MetaOapg.properties.occurred_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addons"]) -> 'SourceUpdateSubscriptionRequestAddons': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discount"]) -> MetaOapg.properties.discount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["plan_oid", "occurred_at", "addons", "quantity", "discount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan_oid"]) -> MetaOapg.properties.plan_oid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["occurred_at"]) -> typing.Union[MetaOapg.properties.occurred_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addons"]) -> typing.Union['SourceUpdateSubscriptionRequestAddons', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> typing.Union[MetaOapg.properties.quantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discount"]) -> typing.Union[MetaOapg.properties.discount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["plan_oid", "occurred_at", "addons", "quantity", "discount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        plan_oid: typing.Union[MetaOapg.properties.plan_oid, str, ],
        occurred_at: typing.Union[MetaOapg.properties.occurred_at, str, datetime, schemas.Unset] = schemas.unset,
        addons: typing.Union['SourceUpdateSubscriptionRequestAddons', schemas.Unset] = schemas.unset,
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        discount: typing.Union[MetaOapg.properties.discount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceUpdateSubscriptionRequest':
        return super().__new__(
            cls,
            *args,
            plan_oid=plan_oid,
            occurred_at=occurred_at,
            addons=addons,
            quantity=quantity,
            discount=discount,
            _configuration=_configuration,
            **kwargs,
        )

from baremetrics_python_sdk.model.source_update_subscription_request_addons import SourceUpdateSubscriptionRequestAddons