import typing
from .sqs import SQSEvent
from .sns import SNSEvent
from .ses import SimpleEmailEvent
from .s3 import S3ObjectLambdaEvent

from dataclasses import dataclass


@dataclass
class BaseOptionalDataClass:
    def __init_subclass__(cls, *args, **kwargs) -> None:
        for field, value in cls.__annotations__.items():
            cls.__annotations__[field] = typing.Optional[value]
            if not hasattr(cls, field):
                setattr(cls, field, None)
        super().__init_subclass__(*args, **kwargs)
