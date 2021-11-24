from dataclasses import dataclass
from typing import Dict, List


@dataclass
class APIGatewayCustomAuthorizerContext:
    principalId: str
    stringKey: str
    numKey: int
    boolKey: bool
    claims: Dict[str, str]


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
class RequestIdentity:
    CognitoIdentityPoolId: str
    AccountId: str
    CognitoIdentityId: str
    Caller: str
    ApiKey: str
    ApiKeyId: str
    AccessKey: str
    SourceIp: str
    CognitoAuthenticationType: str
    CognitoAuthenticationProvider: str
    UserArn: str
    UserAgent: str
    User: str
    ClientCert: ProxyRequestClientCert


@dataclass
class ProxyRequestContext:
    Path: str
    AccountId: str
    ResourceId: str
    Stage: str
    RequestId: str
    Identity: RequestIdentity
    ResourcePath: str
    HttpMethod: str
    ApiId: str
    ExtendedRequestId: str
    ConnectionId: str
    ConnectionAt: int
    DomainName: str
    DomainPrefix: str
    EventType: str
    MessageId: str
    RouteKey: str
    Authorizer: APIGatewayCustomAuthorizerContext
    OperationName: str
    Error: str
    IntegrationLatency: str
    MessageDirection: str
    RequestTime: str
    RequestTimeEpoch: int
    Status: str


@dataclass
class APIGatewayProxyRequest:
    Resource: str
    Path: str
    HttpMethod: str
    Headers: Dict[str, str]
    MultiValueHeaders: Dict[str, List[str]]
    QueryStringParameters: Dict[str, str]
    MultiValueQueryStringParameters: Dict[str, List[str]]
    PathParameters: Dict[str, str]
    StageVariables: Dict[str, str]
    RequestContext: ProxyRequestContext
    Body: str
    IsBase64Encoded: bool