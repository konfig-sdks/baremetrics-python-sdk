import typing_extensions

from baremetrics_python_sdk.paths import PathValues
from baremetrics_python_sdk.apis.paths.v1_account import V1Account
from baremetrics_python_sdk.apis.paths.v1_sources import V1Sources
from baremetrics_python_sdk.apis.paths.v1_source_id_plans import V1SourceIdPlans
from baremetrics_python_sdk.apis.paths.v1_source_id_plans_oid import V1SourceIdPlansOid
from baremetrics_python_sdk.apis.paths.v1_source_id_plans_plan_oid import V1SourceIdPlansPlanOid
from baremetrics_python_sdk.apis.paths.v1_source_id_customers import V1SourceIdCustomers
from baremetrics_python_sdk.apis.paths.v1_source_id_customers_oid import V1SourceIdCustomersOid
from baremetrics_python_sdk.apis.paths.v1_source_id_customers_oid_events import V1SourceIdCustomersOidEvents
from baremetrics_python_sdk.apis.paths.v1_source_id_customers_customer_oid import V1SourceIdCustomersCustomerOid
from baremetrics_python_sdk.apis.paths.v1_source_id_subscriptions import V1SourceIdSubscriptions
from baremetrics_python_sdk.apis.paths.v1_source_id_subscriptions_oid import V1SourceIdSubscriptionsOid
from baremetrics_python_sdk.apis.paths.v1_source_id_subscriptions_subscription_oid import V1SourceIdSubscriptionsSubscriptionOid
from baremetrics_python_sdk.apis.paths.v1_source_id_subscriptions_subscription_oid_cancel import V1SourceIdSubscriptionsSubscriptionOidCancel
from baremetrics_python_sdk.apis.paths.v1_annotations import V1Annotations
from baremetrics_python_sdk.apis.paths.v1_annotations_id import V1AnnotationsId
from baremetrics_python_sdk.apis.paths.v1_goals import V1Goals
from baremetrics_python_sdk.apis.paths.v1_goals_id import V1GoalsId
from baremetrics_python_sdk.apis.paths.v1_users import V1Users
from baremetrics_python_sdk.apis.paths.v1_users_id import V1UsersId
from baremetrics_python_sdk.apis.paths.v1_source_id_charges import V1SourceIdCharges
from baremetrics_python_sdk.apis.paths.v1_source_id_charges_oid import V1SourceIdChargesOid
from baremetrics_python_sdk.apis.paths.v1_source_id_refunds import V1SourceIdRefunds
from baremetrics_python_sdk.apis.paths.v1_source_id_refunds_oid import V1SourceIdRefundsOid
from baremetrics_python_sdk.apis.paths.v1_source_id_events import V1SourceIdEvents
from baremetrics_python_sdk.apis.paths.v1_source_id_events_id import V1SourceIdEventsId
from baremetrics_python_sdk.apis.paths.v1_metrics import V1Metrics
from baremetrics_python_sdk.apis.paths.v1_metrics_metric import V1MetricsMetric
from baremetrics_python_sdk.apis.paths.v1_metrics_metric_customers import V1MetricsMetricCustomers
from baremetrics_python_sdk.apis.paths.v1_metrics_metric_plans import V1MetricsMetricPlans
from baremetrics_python_sdk.apis.paths.v1_metrics_cohorts import V1MetricsCohorts
from baremetrics_python_sdk.apis.paths.v1_segments_fields import V1SegmentsFields
from baremetrics_python_sdk.apis.paths.v1_segments import V1Segments
from baremetrics_python_sdk.apis.paths.v1_segments_id import V1SegmentsId
from baremetrics_python_sdk.apis.paths.v1_segments_search import V1SegmentsSearch
from baremetrics_python_sdk.apis.paths.v1_attributes import V1Attributes
from baremetrics_python_sdk.apis.paths.v1_attributes_fields import V1AttributesFields
from baremetrics_python_sdk.apis.paths.v1_attributes_fields_id import V1AttributesFieldsId
from baremetrics_python_sdk.apis.paths.v1_cancellation_insights_events import V1CancellationInsightsEvents
from baremetrics_python_sdk.apis.paths.v1_cancellation_insights_events_id import V1CancellationInsightsEventsId
from baremetrics_python_sdk.apis.paths.v1_cancellation_insights_reasons_id import V1CancellationInsightsReasonsId
from baremetrics_python_sdk.apis.paths.v1_cancellation_insights_reasons import V1CancellationInsightsReasons

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ACCOUNT: V1Account,
        PathValues.V1_SOURCES: V1Sources,
        PathValues.V1_SOURCE_ID_PLANS: V1SourceIdPlans,
        PathValues.V1_SOURCE_ID_PLANS_OID: V1SourceIdPlansOid,
        PathValues.V1_SOURCE_ID_PLANS_PLAN_OID: V1SourceIdPlansPlanOid,
        PathValues.V1_SOURCE_ID_CUSTOMERS: V1SourceIdCustomers,
        PathValues.V1_SOURCE_ID_CUSTOMERS_OID: V1SourceIdCustomersOid,
        PathValues.V1_SOURCE_ID_CUSTOMERS_OID_EVENTS: V1SourceIdCustomersOidEvents,
        PathValues.V1_SOURCE_ID_CUSTOMERS_CUSTOMER_OID: V1SourceIdCustomersCustomerOid,
        PathValues.V1_SOURCE_ID_SUBSCRIPTIONS: V1SourceIdSubscriptions,
        PathValues.V1_SOURCE_ID_SUBSCRIPTIONS_OID: V1SourceIdSubscriptionsOid,
        PathValues.V1_SOURCE_ID_SUBSCRIPTIONS_SUBSCRIPTION_OID: V1SourceIdSubscriptionsSubscriptionOid,
        PathValues.V1_SOURCE_ID_SUBSCRIPTIONS_SUBSCRIPTION_OID_CANCEL: V1SourceIdSubscriptionsSubscriptionOidCancel,
        PathValues.V1_ANNOTATIONS: V1Annotations,
        PathValues.V1_ANNOTATIONS_ID: V1AnnotationsId,
        PathValues.V1_GOALS: V1Goals,
        PathValues.V1_GOALS_ID: V1GoalsId,
        PathValues.V1_USERS: V1Users,
        PathValues.V1_USERS_ID: V1UsersId,
        PathValues.V1_SOURCE_ID_CHARGES: V1SourceIdCharges,
        PathValues.V1_SOURCE_ID_CHARGES_OID: V1SourceIdChargesOid,
        PathValues.V1_SOURCE_ID_REFUNDS: V1SourceIdRefunds,
        PathValues.V1_SOURCE_ID_REFUNDS_OID: V1SourceIdRefundsOid,
        PathValues.V1_SOURCE_ID_EVENTS: V1SourceIdEvents,
        PathValues.V1_SOURCE_ID_EVENTS_ID: V1SourceIdEventsId,
        PathValues.V1_METRICS: V1Metrics,
        PathValues.V1_METRICS_METRIC: V1MetricsMetric,
        PathValues.V1_METRICS_METRIC_CUSTOMERS: V1MetricsMetricCustomers,
        PathValues.V1_METRICS_METRIC_PLANS: V1MetricsMetricPlans,
        PathValues.V1_METRICS_COHORTS: V1MetricsCohorts,
        PathValues.V1_SEGMENTS_FIELDS: V1SegmentsFields,
        PathValues.V1_SEGMENTS: V1Segments,
        PathValues.V1_SEGMENTS_ID: V1SegmentsId,
        PathValues.V1_SEGMENTS_SEARCH: V1SegmentsSearch,
        PathValues.V1_ATTRIBUTES: V1Attributes,
        PathValues.V1_ATTRIBUTES_FIELDS: V1AttributesFields,
        PathValues.V1_ATTRIBUTES_FIELDS_ID: V1AttributesFieldsId,
        PathValues.V1_CANCELLATION_INSIGHTS_EVENTS: V1CancellationInsightsEvents,
        PathValues.V1_CANCELLATION_INSIGHTS_EVENTS_ID: V1CancellationInsightsEventsId,
        PathValues.V1_CANCELLATION_INSIGHTS_REASONS_ID: V1CancellationInsightsReasonsId,
        PathValues.V1_CANCELLATION_INSIGHTS_REASONS: V1CancellationInsightsReasons,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ACCOUNT: V1Account,
        PathValues.V1_SOURCES: V1Sources,
        PathValues.V1_SOURCE_ID_PLANS: V1SourceIdPlans,
        PathValues.V1_SOURCE_ID_PLANS_OID: V1SourceIdPlansOid,
        PathValues.V1_SOURCE_ID_PLANS_PLAN_OID: V1SourceIdPlansPlanOid,
        PathValues.V1_SOURCE_ID_CUSTOMERS: V1SourceIdCustomers,
        PathValues.V1_SOURCE_ID_CUSTOMERS_OID: V1SourceIdCustomersOid,
        PathValues.V1_SOURCE_ID_CUSTOMERS_OID_EVENTS: V1SourceIdCustomersOidEvents,
        PathValues.V1_SOURCE_ID_CUSTOMERS_CUSTOMER_OID: V1SourceIdCustomersCustomerOid,
        PathValues.V1_SOURCE_ID_SUBSCRIPTIONS: V1SourceIdSubscriptions,
        PathValues.V1_SOURCE_ID_SUBSCRIPTIONS_OID: V1SourceIdSubscriptionsOid,
        PathValues.V1_SOURCE_ID_SUBSCRIPTIONS_SUBSCRIPTION_OID: V1SourceIdSubscriptionsSubscriptionOid,
        PathValues.V1_SOURCE_ID_SUBSCRIPTIONS_SUBSCRIPTION_OID_CANCEL: V1SourceIdSubscriptionsSubscriptionOidCancel,
        PathValues.V1_ANNOTATIONS: V1Annotations,
        PathValues.V1_ANNOTATIONS_ID: V1AnnotationsId,
        PathValues.V1_GOALS: V1Goals,
        PathValues.V1_GOALS_ID: V1GoalsId,
        PathValues.V1_USERS: V1Users,
        PathValues.V1_USERS_ID: V1UsersId,
        PathValues.V1_SOURCE_ID_CHARGES: V1SourceIdCharges,
        PathValues.V1_SOURCE_ID_CHARGES_OID: V1SourceIdChargesOid,
        PathValues.V1_SOURCE_ID_REFUNDS: V1SourceIdRefunds,
        PathValues.V1_SOURCE_ID_REFUNDS_OID: V1SourceIdRefundsOid,
        PathValues.V1_SOURCE_ID_EVENTS: V1SourceIdEvents,
        PathValues.V1_SOURCE_ID_EVENTS_ID: V1SourceIdEventsId,
        PathValues.V1_METRICS: V1Metrics,
        PathValues.V1_METRICS_METRIC: V1MetricsMetric,
        PathValues.V1_METRICS_METRIC_CUSTOMERS: V1MetricsMetricCustomers,
        PathValues.V1_METRICS_METRIC_PLANS: V1MetricsMetricPlans,
        PathValues.V1_METRICS_COHORTS: V1MetricsCohorts,
        PathValues.V1_SEGMENTS_FIELDS: V1SegmentsFields,
        PathValues.V1_SEGMENTS: V1Segments,
        PathValues.V1_SEGMENTS_ID: V1SegmentsId,
        PathValues.V1_SEGMENTS_SEARCH: V1SegmentsSearch,
        PathValues.V1_ATTRIBUTES: V1Attributes,
        PathValues.V1_ATTRIBUTES_FIELDS: V1AttributesFields,
        PathValues.V1_ATTRIBUTES_FIELDS_ID: V1AttributesFieldsId,
        PathValues.V1_CANCELLATION_INSIGHTS_EVENTS: V1CancellationInsightsEvents,
        PathValues.V1_CANCELLATION_INSIGHTS_EVENTS_ID: V1CancellationInsightsEventsId,
        PathValues.V1_CANCELLATION_INSIGHTS_REASONS_ID: V1CancellationInsightsReasonsId,
        PathValues.V1_CANCELLATION_INSIGHTS_REASONS: V1CancellationInsightsReasons,
    }
)
