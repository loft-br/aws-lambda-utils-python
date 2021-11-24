from dataclasses import dataclass
from typing import Dict, List, Sequence


@dataclass
class JwtDescription:
    Claims: Dict[str, str]
    Scopes: Sequence[str]


@dataclass
class CognitoIdentityDescription:
    AMR: List[str]
    IdentityId: str
    IdentityPoolId: str


@dataclass
class IAMDescription:
    AccessKey: str
    AccountId: str
    CallerId: str
    CognitoIdentity: CognitoIdentityDescription
    PrincipalOrgId: str
    UserARN: str
    UserId: str


@dataclass
class AuthorizerDescription:
    Jwt: JwtDescription
    Lambda: Dict[str, str]
    IAM: IAMDescription


@dataclass
class HttpDescription:
    Method: str
    Path: str
    Protocol: str
    SourceIp: str
    UserAgent: str


@dataclass
class ClientCertValidity:
    NotBefore: str
    NotAfter: str


@dataclass
class ProxyRequestClientCert:
    ClientCertPem: str
    SubjectDN: str
    IssuerDN: str
    SerialNumber: str
    Validity: ClientCertValidity


@dataclass
class ProxyRequestAuthentication:
    ClientCert: ProxyRequestClientCert


@dataclass
class ProxyRequestContext:
    AccountId: str
    ApiId: str
    Authorizer: AuthorizerDescription
    DomainName: str
    DomainPrefix: str
    Http: HttpDescription
    RequestId: str
    RouteId: str
    RouteKey: str
    Stage: str
    Time: str
    TimeEpoch: int
    Authentication: ProxyRequestAuthentication


@dataclass
class APIGatewayHttpApiV2ProxyRequest:
    Version: str
    RouteKey: str
    RawPath: str
    RawQueryString: str
    Cookies: Sequence[str]
    Headers: Dict[str, str]
    QueryStringParameters: Dict[str, str]
    RequestContext: ProxyRequestContext
    Body: str
    PathParameters: Dict[str, str]
    IsBase64Encoded: bool
    StageVariables: Dict[str, str]
