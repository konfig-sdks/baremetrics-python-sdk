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


class AttributeSetPropertiesRequestAttributesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "field_id",
            "customer_oid",
            "customer_email",
            "value",
        }
        
        class properties:
            customer_oid = schemas.StrSchema
            customer_email = schemas.StrSchema
            field_id = schemas.StrSchema
            value = schemas.StrSchema
            __annotations__ = {
                "customer_oid": customer_oid,
                "customer_email": customer_email,
                "field_id": field_id,
                "value": value,
            }
    
    field_id: MetaOapg.properties.field_id
    customer_oid: MetaOapg.properties.customer_oid
    customer_email: MetaOapg.properties.customer_email
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_oid"]) -> MetaOapg.properties.customer_oid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_email"]) -> MetaOapg.properties.customer_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_id"]) -> MetaOapg.properties.field_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customer_oid", "customer_email", "field_id", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_oid"]) -> MetaOapg.properties.customer_oid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_email"]) -> MetaOapg.properties.customer_email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_id"]) -> MetaOapg.properties.field_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customer_oid", "customer_email", "field_id", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        field_id: typing.Union[MetaOapg.properties.field_id, str, ],
        customer_oid: typing.Union[MetaOapg.properties.customer_oid, str, ],
        customer_email: typing.Union[MetaOapg.properties.customer_email, str, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttributeSetPropertiesRequestAttributesItem':
        return super().__new__(
            cls,
            *args,
            field_id=field_id,
            customer_oid=customer_oid,
            customer_email=customer_email,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )
