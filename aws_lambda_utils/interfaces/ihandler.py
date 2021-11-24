from abc import ABC, abstractmethod
from typing import Any, TypeVar
from ..events import SQSEvent, SNSEvent, S3ObjectLambdaEvent, SimpleEmailEvent
from .icontext import IContext

Event = TypeVar(
    "Event",
    SQSEvent,
    SNSEvent,
    S3ObjectLambdaEvent,
    SimpleEmailEvent,
)


class IHandler(ABC):
    @staticmethod
    @abstractmethod
    def handler(event: Event, context: IContext) -> Any:
        ...
