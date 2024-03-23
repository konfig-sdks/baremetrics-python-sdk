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


class MetricShowSummaryResponseMetricsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            human_date = schemas.StrSchema
            date = schemas.IntSchema
            active_customers = schemas.IntSchema
            active_subscriptions = schemas.IntSchema
            add_on_mrr = schemas.IntSchema
            arpu = schemas.IntSchema
            arr = schemas.IntSchema
            cancellations = schemas.IntSchema
            coupons = schemas.IntSchema
            downgrades = schemas.IntSchema
            failed_charges = schemas.IntSchema
            fees = schemas.IntSchema
            ltv = schemas.IntSchema
            mrr = schemas.IntSchema
            net_revenue = schemas.IntSchema
            new_customers = schemas.IntSchema
            other_revenue = schemas.IntSchema
            reactivated_customers = schemas.IntSchema
            refunds = schemas.IntSchema
            revenue_churn = schemas.IntSchema
            trial_conversions = schemas.IntSchema
            upgrades = schemas.IntSchema
            user_churn = schemas.IntSchema
            __annotations__ = {
                "human_date": human_date,
                "date": date,
                "active_customers": active_customers,
                "active_subscriptions": active_subscriptions,
                "add_on_mrr": add_on_mrr,
                "arpu": arpu,
                "arr": arr,
                "cancellations": cancellations,
                "coupons": coupons,
                "downgrades": downgrades,
                "failed_charges": failed_charges,
                "fees": fees,
                "ltv": ltv,
                "mrr": mrr,
                "net_revenue": net_revenue,
                "new_customers": new_customers,
                "other_revenue": other_revenue,
                "reactivated_customers": reactivated_customers,
                "refunds": refunds,
                "revenue_churn": revenue_churn,
                "trial_conversions": trial_conversions,
                "upgrades": upgrades,
                "user_churn": user_churn,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["human_date"]) -> MetaOapg.properties.human_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_customers"]) -> MetaOapg.properties.active_customers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_subscriptions"]) -> MetaOapg.properties.active_subscriptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["add_on_mrr"]) -> MetaOapg.properties.add_on_mrr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arpu"]) -> MetaOapg.properties.arpu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arr"]) -> MetaOapg.properties.arr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancellations"]) -> MetaOapg.properties.cancellations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coupons"]) -> MetaOapg.properties.coupons: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["downgrades"]) -> MetaOapg.properties.downgrades: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failed_charges"]) -> MetaOapg.properties.failed_charges: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fees"]) -> MetaOapg.properties.fees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ltv"]) -> MetaOapg.properties.ltv: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mrr"]) -> MetaOapg.properties.mrr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_revenue"]) -> MetaOapg.properties.net_revenue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["new_customers"]) -> MetaOapg.properties.new_customers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other_revenue"]) -> MetaOapg.properties.other_revenue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactivated_customers"]) -> MetaOapg.properties.reactivated_customers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refunds"]) -> MetaOapg.properties.refunds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenue_churn"]) -> MetaOapg.properties.revenue_churn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trial_conversions"]) -> MetaOapg.properties.trial_conversions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upgrades"]) -> MetaOapg.properties.upgrades: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_churn"]) -> MetaOapg.properties.user_churn: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["human_date", "date", "active_customers", "active_subscriptions", "add_on_mrr", "arpu", "arr", "cancellations", "coupons", "downgrades", "failed_charges", "fees", "ltv", "mrr", "net_revenue", "new_customers", "other_revenue", "reactivated_customers", "refunds", "revenue_churn", "trial_conversions", "upgrades", "user_churn", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["human_date"]) -> typing.Union[MetaOapg.properties.human_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_customers"]) -> typing.Union[MetaOapg.properties.active_customers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_subscriptions"]) -> typing.Union[MetaOapg.properties.active_subscriptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["add_on_mrr"]) -> typing.Union[MetaOapg.properties.add_on_mrr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arpu"]) -> typing.Union[MetaOapg.properties.arpu, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arr"]) -> typing.Union[MetaOapg.properties.arr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancellations"]) -> typing.Union[MetaOapg.properties.cancellations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coupons"]) -> typing.Union[MetaOapg.properties.coupons, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["downgrades"]) -> typing.Union[MetaOapg.properties.downgrades, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failed_charges"]) -> typing.Union[MetaOapg.properties.failed_charges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fees"]) -> typing.Union[MetaOapg.properties.fees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ltv"]) -> typing.Union[MetaOapg.properties.ltv, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mrr"]) -> typing.Union[MetaOapg.properties.mrr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_revenue"]) -> typing.Union[MetaOapg.properties.net_revenue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["new_customers"]) -> typing.Union[MetaOapg.properties.new_customers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other_revenue"]) -> typing.Union[MetaOapg.properties.other_revenue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactivated_customers"]) -> typing.Union[MetaOapg.properties.reactivated_customers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refunds"]) -> typing.Union[MetaOapg.properties.refunds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenue_churn"]) -> typing.Union[MetaOapg.properties.revenue_churn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trial_conversions"]) -> typing.Union[MetaOapg.properties.trial_conversions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upgrades"]) -> typing.Union[MetaOapg.properties.upgrades, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_churn"]) -> typing.Union[MetaOapg.properties.user_churn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["human_date", "date", "active_customers", "active_subscriptions", "add_on_mrr", "arpu", "arr", "cancellations", "coupons", "downgrades", "failed_charges", "fees", "ltv", "mrr", "net_revenue", "new_customers", "other_revenue", "reactivated_customers", "refunds", "revenue_churn", "trial_conversions", "upgrades", "user_churn", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        human_date: typing.Union[MetaOapg.properties.human_date, str, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active_customers: typing.Union[MetaOapg.properties.active_customers, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active_subscriptions: typing.Union[MetaOapg.properties.active_subscriptions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        add_on_mrr: typing.Union[MetaOapg.properties.add_on_mrr, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        arpu: typing.Union[MetaOapg.properties.arpu, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        arr: typing.Union[MetaOapg.properties.arr, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cancellations: typing.Union[MetaOapg.properties.cancellations, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        coupons: typing.Union[MetaOapg.properties.coupons, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        downgrades: typing.Union[MetaOapg.properties.downgrades, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        failed_charges: typing.Union[MetaOapg.properties.failed_charges, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fees: typing.Union[MetaOapg.properties.fees, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ltv: typing.Union[MetaOapg.properties.ltv, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        mrr: typing.Union[MetaOapg.properties.mrr, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        net_revenue: typing.Union[MetaOapg.properties.net_revenue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        new_customers: typing.Union[MetaOapg.properties.new_customers, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        other_revenue: typing.Union[MetaOapg.properties.other_revenue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reactivated_customers: typing.Union[MetaOapg.properties.reactivated_customers, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        refunds: typing.Union[MetaOapg.properties.refunds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        revenue_churn: typing.Union[MetaOapg.properties.revenue_churn, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trial_conversions: typing.Union[MetaOapg.properties.trial_conversions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        upgrades: typing.Union[MetaOapg.properties.upgrades, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        user_churn: typing.Union[MetaOapg.properties.user_churn, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MetricShowSummaryResponseMetricsItem':
        return super().__new__(
            cls,
            *args,
            human_date=human_date,
            date=date,
            active_customers=active_customers,
            active_subscriptions=active_subscriptions,
            add_on_mrr=add_on_mrr,
            arpu=arpu,
            arr=arr,
            cancellations=cancellations,
            coupons=coupons,
            downgrades=downgrades,
            failed_charges=failed_charges,
            fees=fees,
            ltv=ltv,
            mrr=mrr,
            net_revenue=net_revenue,
            new_customers=new_customers,
            other_revenue=other_revenue,
            reactivated_customers=reactivated_customers,
            refunds=refunds,
            revenue_churn=revenue_churn,
            trial_conversions=trial_conversions,
            upgrades=upgrades,
            user_churn=user_churn,
            _configuration=_configuration,
            **kwargs,
        )