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


class SourceUpdateCustomerInformationResponseCustomerCurrentPlansItem(
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
            name = schemas.StrSchema
            interval = schemas.StrSchema
            interval_count = schemas.IntSchema
            trial_duration = schemas.AnyTypeSchema
            trial_duration_unit = schemas.AnyTypeSchema
            created = schemas.IntSchema
            active = schemas.BoolSchema
            setup_fees = schemas.IntSchema
        
            @staticmethod
            def amounts() -> typing.Type['SourceUpdateCustomerInformationResponseCustomerCurrentPlansItemAmounts']:
                return SourceUpdateCustomerInformationResponseCustomerCurrentPlansItemAmounts
            __annotations__ = {
                "oid": oid,
                "source_id": source_id,
                "source": source,
                "name": name,
                "interval": interval,
                "interval_count": interval_count,
                "trial_duration": trial_duration,
                "trial_duration_unit": trial_duration_unit,
                "created": created,
                "active": active,
                "setup_fees": setup_fees,
                "amounts": amounts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oid"]) -> MetaOapg.properties.oid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> MetaOapg.properties.source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval"]) -> MetaOapg.properties.interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval_count"]) -> MetaOapg.properties.interval_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trial_duration"]) -> MetaOapg.properties.trial_duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trial_duration_unit"]) -> MetaOapg.properties.trial_duration_unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["setup_fees"]) -> MetaOapg.properties.setup_fees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amounts"]) -> 'SourceUpdateCustomerInformationResponseCustomerCurrentPlansItemAmounts': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["oid", "source_id", "source", "name", "interval", "interval_count", "trial_duration", "trial_duration_unit", "created", "active", "setup_fees", "amounts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oid"]) -> typing.Union[MetaOapg.properties.oid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union[MetaOapg.properties.source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval"]) -> typing.Union[MetaOapg.properties.interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval_count"]) -> typing.Union[MetaOapg.properties.interval_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trial_duration"]) -> typing.Union[MetaOapg.properties.trial_duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trial_duration_unit"]) -> typing.Union[MetaOapg.properties.trial_duration_unit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["setup_fees"]) -> typing.Union[MetaOapg.properties.setup_fees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amounts"]) -> typing.Union['SourceUpdateCustomerInformationResponseCustomerCurrentPlansItemAmounts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["oid", "source_id", "source", "name", "interval", "interval_count", "trial_duration", "trial_duration_unit", "created", "active", "setup_fees", "amounts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        oid: typing.Union[MetaOapg.properties.oid, str, schemas.Unset] = schemas.unset,
        source_id: typing.Union[MetaOapg.properties.source_id, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        interval: typing.Union[MetaOapg.properties.interval, str, schemas.Unset] = schemas.unset,
        interval_count: typing.Union[MetaOapg.properties.interval_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trial_duration: typing.Union[MetaOapg.properties.trial_duration, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        trial_duration_unit: typing.Union[MetaOapg.properties.trial_duration_unit, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        setup_fees: typing.Union[MetaOapg.properties.setup_fees, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        amounts: typing.Union['SourceUpdateCustomerInformationResponseCustomerCurrentPlansItemAmounts', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceUpdateCustomerInformationResponseCustomerCurrentPlansItem':
        return super().__new__(
            cls,
            *args,
            oid=oid,
            source_id=source_id,
            source=source,
            name=name,
            interval=interval,
            interval_count=interval_count,
            trial_duration=trial_duration,
            trial_duration_unit=trial_duration_unit,
            created=created,
            active=active,
            setup_fees=setup_fees,
            amounts=amounts,
            _configuration=_configuration,
            **kwargs,
        )

from baremetrics_python_sdk.model.source_update_customer_information_response_customer_current_plans_item_amounts import SourceUpdateCustomerInformationResponseCustomerCurrentPlansItemAmounts
