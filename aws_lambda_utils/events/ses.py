from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class SimpleEmailVerdict:
    Status: str


@dataclass
class SimpleEmailCommonHeaders:
    From: List[str]
    To: List[str]
    ReturnPath: str
    MessageId: str
    Date: str
    Subject: str


@dataclass
class SimpleEmailHeader:
    Name: str
    Value: str


@dataclass
class ReceiptAction:
    Type: str


@dataclass
class SimpleEmailReceipt:
    Recipients: List[str]
    Timestamp: datetime
    SpamVerdict: SimpleEmailVerdict
    DKIMVerdict: SimpleEmailVerdict
    SPFVerdict: SimpleEmailVerdict
    VirusVerdict: SimpleEmailVerdict
    DMARCVerdict: SimpleEmailVerdict
    Action: ReceiptAction
    ProcessingTimeMillis: int


@dataclass
class SimpleEmailMessage:
    CommonHeaders: SimpleEmailCommonHeaders
    Source: str
    Timestamp: datetime
    Destination: List[str]
    Headers: List[SimpleEmailHeader]
    HeadersTruncated: bool
    MessageId: str


@dataclass
class SimpleEmailService:
    Mail: SimpleEmailMessage
    Receipt: SimpleEmailReceipt


@dataclass
class SimpleEmailRecord:
    EventVersion: str
    EventSource: str
    Ses: SimpleEmailService


@dataclass
class SimpleEmailEvent:
    Records: List[SimpleEmailRecord]
