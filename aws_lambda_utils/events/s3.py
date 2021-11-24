from dataclasses import dataclass
from typing import Dict


@dataclass
class ConfigurationType:
    AccessPointArn: str
    SupportingAccessPointArn: str
    Payload: str


@dataclass
class GetObjectContextType:
    InputS3Url: str
    OutputRoute: str
    OutputToken: str


@dataclass
class SessionContextAttributesType:
    MfaAuthenticated: str
    CreationDate: str


@dataclass
class SessionIssuerType:
    Type: str
    PrincipalId: str
    Arn: str
    AccountId: str
    UserName: str


@dataclass
class SessionContextType:
    Attributes: SessionContextAttributesType
    SessionIssuer: SessionIssuerType


@dataclass
class UserIdentityType:
    Type: str
    PrincipalId: str
    Arn: str
    AccountId: str
    AccessKeyId: str
    SessionContext: SessionContextType


@dataclass
class UserRequestType:
    Url: str
    Headers: Dict[str, str]


@dataclass
class S3ObjectLambdaEvent:
    XAmzRequestId: str
    GetObjectContext: GetObjectContextType
    Configuration: ConfigurationType
    UserRequest: UserRequestType
    UserIdentity: UserIdentityType
    ProtocolVersion: str
