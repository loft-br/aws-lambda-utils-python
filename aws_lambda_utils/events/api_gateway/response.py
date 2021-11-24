from dataclasses import dataclass
from typing import Dict, List
from . import BaseOptionalDataClass


@dataclass
class APIGatewayProxyResponse(BaseOptionalDataClass):
    StatusCode: int
    Headers: Dict[str, str]
    MultiValueHeaders: Dict[str, List[str]]
    Body: str
    IsBase64Encoded: bool
