import typing_extensions

from baremetrics_python_sdk.apis.tags import TagValues
from baremetrics_python_sdk.apis.tags.source_api import SourceApi
from baremetrics_python_sdk.apis.tags.segment_api import SegmentApi
from baremetrics_python_sdk.apis.tags.metric_api import MetricApi
from baremetrics_python_sdk.apis.tags.annotation_api import AnnotationApi
from baremetrics_python_sdk.apis.tags.goal_api import GoalApi
from baremetrics_python_sdk.apis.tags.attribute_api import AttributeApi
from baremetrics_python_sdk.apis.tags.event_api import EventApi
from baremetrics_python_sdk.apis.tags.reason_api import ReasonApi
from baremetrics_python_sdk.apis.tags.user_api import UserApi
from baremetrics_python_sdk.apis.tags.account_api import AccountApi
from baremetrics_python_sdk.apis.tags.cancellation_insight_api import CancellationInsightApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SOURCE: SourceApi,
        TagValues.SEGMENT: SegmentApi,
        TagValues.METRIC: MetricApi,
        TagValues.ANNOTATION: AnnotationApi,
        TagValues.GOAL: GoalApi,
        TagValues.ATTRIBUTE: AttributeApi,
        TagValues.EVENT: EventApi,
        TagValues.REASON: ReasonApi,
        TagValues.USER: UserApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.CANCELLATION_INSIGHT: CancellationInsightApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SOURCE: SourceApi,
        TagValues.SEGMENT: SegmentApi,
        TagValues.METRIC: MetricApi,
        TagValues.ANNOTATION: AnnotationApi,
        TagValues.GOAL: GoalApi,
        TagValues.ATTRIBUTE: AttributeApi,
        TagValues.EVENT: EventApi,
        TagValues.REASON: ReasonApi,
        TagValues.USER: UserApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.CANCELLATION_INSIGHT: CancellationInsightApi,
    }
)
