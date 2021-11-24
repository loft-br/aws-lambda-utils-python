from dataclasses import dataclass
from typing import Dict, List, Sequence


@dataclass
class APIGatewayProxyResponse:
    StatusCode: int
    Headers: Dict[str, str]
    MultiValueHeaders: Dict[str, List[str]]
    Body: str
    IsBase64Encoded: bool
