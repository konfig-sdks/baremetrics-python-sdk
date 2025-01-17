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


class AnnotationListResponseAnnotationsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            metric = schemas.StrSchema
            annotation = schemas.StrSchema
            date = schemas.StrSchema
            _global = schemas.BoolSchema
        
            @staticmethod
            def user() -> typing.Type['AnnotationListResponseAnnotationsItemUser']:
                return AnnotationListResponseAnnotationsItemUser
            __annotations__ = {
                "id": id,
                "metric": metric,
                "annotation": annotation,
                "date": date,
                "global": _global,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metric"]) -> MetaOapg.properties.metric: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annotation"]) -> MetaOapg.properties.annotation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["global"]) -> MetaOapg.properties._global: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'AnnotationListResponseAnnotationsItemUser': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "metric", "annotation", "date", "global", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metric"]) -> typing.Union[MetaOapg.properties.metric, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annotation"]) -> typing.Union[MetaOapg.properties.annotation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["global"]) -> typing.Union[MetaOapg.properties._global, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['AnnotationListResponseAnnotationsItemUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "metric", "annotation", "date", "global", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        metric: typing.Union[MetaOapg.properties.metric, str, schemas.Unset] = schemas.unset,
        annotation: typing.Union[MetaOapg.properties.annotation, str, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        user: typing.Union['AnnotationListResponseAnnotationsItemUser', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AnnotationListResponseAnnotationsItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            metric=metric,
            annotation=annotation,
            date=date,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from baremetrics_python_sdk.model.annotation_list_response_annotations_item_user import AnnotationListResponseAnnotationsItemUser
