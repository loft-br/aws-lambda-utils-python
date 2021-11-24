from dataclasses import dataclass
from typing import Dict, List
from .common import MessageAttribute
from datetime import datetime


@dataclass
class SNSMessage:
    Message: str
    MessageAttributes: Dict[str, MessageAttribute]
    MessageId: str
    Signature: str
    SignatureVersion: str
    SigningCertUrl: str
    Subject: str
    Timestamp: datetime
    TopicArn: str
    Type: str
    UnsubscribeUrl: str


@dataclass
class SNSRecord:
    EventSource: str
    EventSubscriptionArn: str
    EventVersion: str
    Sns: SNSMessage


@dataclass
class SNSEvent:
    Records: List[SNSRecord]
