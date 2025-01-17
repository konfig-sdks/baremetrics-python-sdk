# coding: utf-8

"""
    Production

    Baremetrics provides real-time subscription metrics for teams built with Stripe, Shopify Partners, Braintree, Recurly, Chargebee, Google Play, and App Store Connect.   In addition to metrics, Baremetrics provides tools that help you reduce churn and grow your business faster:   Recover: Prevent failed charges and keep your hard-earned revenue with our 100% automated toolkit.   Cancellation insights: Learn exactly why your customers cancel, calculate lost revenue by cancellation reason, and send automated emails to win customers back.  Flightpath: Plan for the future with flexible financial modeling tools built for growing SaaS companies.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from baremetrics_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from baremetrics_python_sdk.api_response import AsyncGeneratorResponse
from baremetrics_python_sdk import api_client, exceptions
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

from baremetrics_python_sdk.model.segment_find_without_save_response import SegmentFindWithoutSaveResponse as SegmentFindWithoutSaveResponseSchema
from baremetrics_python_sdk.model.segment_find_without_save_request_query import SegmentFindWithoutSaveRequestQuery as SegmentFindWithoutSaveRequestQuerySchema
from baremetrics_python_sdk.model.segment_find_without_save_request import SegmentFindWithoutSaveRequest as SegmentFindWithoutSaveRequestSchema

from baremetrics_python_sdk.type.segment_find_without_save_response import SegmentFindWithoutSaveResponse
from baremetrics_python_sdk.type.segment_find_without_save_request_query import SegmentFindWithoutSaveRequestQuery
from baremetrics_python_sdk.type.segment_find_without_save_request import SegmentFindWithoutSaveRequest

from ...api_client import Dictionary
from baremetrics_python_sdk.pydantic.segment_find_without_save_request import SegmentFindWithoutSaveRequest as SegmentFindWithoutSaveRequestPydantic
from baremetrics_python_sdk.pydantic.segment_find_without_save_response import SegmentFindWithoutSaveResponse as SegmentFindWithoutSaveResponsePydantic
from baremetrics_python_sdk.pydantic.segment_find_without_save_request_query import SegmentFindWithoutSaveRequestQuery as SegmentFindWithoutSaveRequestQueryPydantic

# Query params
PerPageSchema = schemas.Int32Schema
PageSchema = schemas.Int32Schema
SortSchema = schemas.StrSchema
OrderSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'per_page': typing.Union[PerPageSchema, decimal.Decimal, int, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'sort': typing.Union[SortSchema, str, ],
        'order': typing.Union[OrderSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_per_page = api_client.QueryParameter(
    name="per_page",
    style=api_client.ParameterStyle.FORM,
    schema=PerPageSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_order = api_client.QueryParameter(
    name="order",
    style=api_client.ParameterStyle.FORM,
    schema=OrderSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = SegmentFindWithoutSaveRequestSchema


request_body_segment_find_without_save_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = SegmentFindWithoutSaveResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SegmentFindWithoutSaveResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SegmentFindWithoutSaveResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _find_without_save_mapped_args(
        self,
        query: SegmentFindWithoutSaveRequestQuery,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if query is not None:
            _body["query"] = query
        args.body = _body
        if per_page is not None:
            _query_params["per_page"] = per_page
        if page is not None:
            _query_params["page"] = page
        if sort is not None:
            _query_params["sort"] = sort
        if order is not None:
            _query_params["order"] = order
        args.query = _query_params
        return args

    async def _afind_without_save_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Search Segment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_per_page,
            request_query_page,
            request_query_sort,
            request_query_order,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/segments/search',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_segment_find_without_save_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _find_without_save_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Search Segment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_per_page,
            request_query_page,
            request_query_sort,
            request_query_order,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/segments/search',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_segment_find_without_save_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class FindWithoutSaveRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afind_without_save(
        self,
        query: SegmentFindWithoutSaveRequestQuery,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_without_save_mapped_args(
            query=query,
            per_page=per_page,
            page=page,
            sort=sort,
            order=order,
        )
        return await self._afind_without_save_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def find_without_save(
        self,
        query: SegmentFindWithoutSaveRequestQuery,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_without_save_mapped_args(
            query=query,
            per_page=per_page,
            page=page,
            sort=sort,
            order=order,
        )
        return self._find_without_save_oapg(
            body=args.body,
            query_params=args.query,
        )

class FindWithoutSave(BaseApi):

    async def afind_without_save(
        self,
        query: SegmentFindWithoutSaveRequestQuery,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> SegmentFindWithoutSaveResponsePydantic:
        raw_response = await self.raw.afind_without_save(
            query=query,
            per_page=per_page,
            page=page,
            sort=sort,
            order=order,
            **kwargs,
        )
        if validate:
            return SegmentFindWithoutSaveResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SegmentFindWithoutSaveResponsePydantic, raw_response.body)
    
    
    def find_without_save(
        self,
        query: SegmentFindWithoutSaveRequestQuery,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        validate: bool = False,
    ) -> SegmentFindWithoutSaveResponsePydantic:
        raw_response = self.raw.find_without_save(
            query=query,
            per_page=per_page,
            page=page,
            sort=sort,
            order=order,
        )
        if validate:
            return SegmentFindWithoutSaveResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SegmentFindWithoutSaveResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        query: SegmentFindWithoutSaveRequestQuery,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_without_save_mapped_args(
            query=query,
            per_page=per_page,
            page=page,
            sort=sort,
            order=order,
        )
        return await self._afind_without_save_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        query: SegmentFindWithoutSaveRequestQuery,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_without_save_mapped_args(
            query=query,
            per_page=per_page,
            page=page,
            sort=sort,
            order=order,
        )
        return self._find_without_save_oapg(
            body=args.body,
            query_params=args.query,
        )

