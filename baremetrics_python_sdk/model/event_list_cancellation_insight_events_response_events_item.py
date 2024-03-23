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


class EventListCancellationInsightEventsResponseEventsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            comment = schemas.AnyTypeSchema
            created_at = schemas.IntSchema
        
            @staticmethod
            def subscriptions() -> typing.Type['EventListCancellationInsightEventsResponseEventsItemSubscriptions']:
                return EventListCancellationInsightEventsResponseEventsItemSubscriptions
        
            @staticmethod
            def reason() -> typing.Type['EventListCancellationInsightEventsResponseEventsItemReason']:
                return EventListCancellationInsightEventsResponseEventsItemReason
        
            @staticmethod
            def customer() -> typing.Type['EventListCancellationInsightEventsResponseEventsItemCustomer']:
                return EventListCancellationInsightEventsResponseEventsItemCustomer
            __annotations__ = {
                "id": id,
                "comment": comment,
                "created_at": created_at,
                "subscriptions": subscriptions,
                "reason": reason,
                "customer": customer,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriptions"]) -> 'EventListCancellationInsightEventsResponseEventsItemSubscriptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> 'EventListCancellationInsightEventsResponseEventsItemReason': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'EventListCancellationInsightEventsResponseEventsItemCustomer': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "comment", "created_at", "subscriptions", "reason", "customer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriptions"]) -> typing.Union['EventListCancellationInsightEventsResponseEventsItemSubscriptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union['EventListCancellationInsightEventsResponseEventsItemReason', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['EventListCancellationInsightEventsResponseEventsItemCustomer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "comment", "created_at", "subscriptions", "reason", "customer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        subscriptions: typing.Union['EventListCancellationInsightEventsResponseEventsItemSubscriptions', schemas.Unset] = schemas.unset,
        reason: typing.Union['EventListCancellationInsightEventsResponseEventsItemReason', schemas.Unset] = schemas.unset,
        customer: typing.Union['EventListCancellationInsightEventsResponseEventsItemCustomer', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventListCancellationInsightEventsResponseEventsItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            comment=comment,
            created_at=created_at,
            subscriptions=subscriptions,
            reason=reason,
            customer=customer,
            _configuration=_configuration,
            **kwargs,
        )

from baremetrics_python_sdk.model.event_list_cancellation_insight_events_response_events_item_customer import EventListCancellationInsightEventsResponseEventsItemCustomer
from baremetrics_python_sdk.model.event_list_cancellation_insight_events_response_events_item_reason import EventListCancellationInsightEventsResponseEventsItemReason
from baremetrics_python_sdk.model.event_list_cancellation_insight_events_response_events_item_subscriptions import EventListCancellationInsightEventsResponseEventsItemSubscriptions
