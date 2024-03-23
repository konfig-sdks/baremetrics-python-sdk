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


class EventListCancellationInsightEventsResponseEventsItemCustomer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            oid = schemas.StrSchema
            source_id = schemas.StrSchema
            source = schemas.StrSchema
            created = schemas.IntSchema
            email = schemas.StrSchema
            name = schemas.StrSchema
            display_image = schemas.StrSchema
            display_name = schemas.StrSchema
            notes = schemas.AnyTypeSchema
            ltv = schemas.IntSchema
            __annotations__ = {
                "oid": oid,
                "source_id": source_id,
                "source": source,
                "created": created,
                "email": email,
                "name": name,
                "display_image": display_image,
                "display_name": display_name,
                "notes": notes,
                "ltv": ltv,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oid"]) -> MetaOapg.properties.oid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> MetaOapg.properties.source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_image"]) -> MetaOapg.properties.display_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ltv"]) -> MetaOapg.properties.ltv: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["oid", "source_id", "source", "created", "email", "name", "display_image", "display_name", "notes", "ltv", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oid"]) -> typing.Union[MetaOapg.properties.oid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union[MetaOapg.properties.source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_image"]) -> typing.Union[MetaOapg.properties.display_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ltv"]) -> typing.Union[MetaOapg.properties.ltv, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["oid", "source_id", "source", "created", "email", "name", "display_image", "display_name", "notes", "ltv", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        oid: typing.Union[MetaOapg.properties.oid, str, schemas.Unset] = schemas.unset,
        source_id: typing.Union[MetaOapg.properties.source_id, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        display_image: typing.Union[MetaOapg.properties.display_image, str, schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        ltv: typing.Union[MetaOapg.properties.ltv, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventListCancellationInsightEventsResponseEventsItemCustomer':
        return super().__new__(
            cls,
            *args,
            oid=oid,
            source_id=source_id,
            source=source,
            created=created,
            email=email,
            name=name,
            display_image=display_image,
            display_name=display_name,
            notes=notes,
            ltv=ltv,
            _configuration=_configuration,
            **kwargs,
        )
