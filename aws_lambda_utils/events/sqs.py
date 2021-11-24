from dataclasses import dataclass
from typing import Dict, List
from mypy_boto3_sqs.type_defs import MessageAttributeValueTypeDef


@dataclass
class SQSRecord:
    MessageId: str
    ReceiptHandle: str
    Body: str
    Md5OfBody: str
    Md5OfMessageAttributes: str
    EventSourceArn: str
    EventSource: str
    AwsRegion: str
    Attributes: Dict[str, str]
    MessageAttributes: Dict[str, MessageAttributeValueTypeDef]


@dataclass
class SQSEvent:
    Records: List[SQSRecord]
