# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from baremetrics_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SOURCE = "Source"
    SEGMENT = "Segment"
    METRIC = "Metric"
    ANNOTATION = "Annotation"
    GOAL = "Goal"
    ATTRIBUTE = "Attribute"
    EVENT = "Event"
    REASON = "Reason"
    USER = "User"
    ACCOUNT = "Account"
    CANCELLATION_INSIGHT = "CancellationInsight"
