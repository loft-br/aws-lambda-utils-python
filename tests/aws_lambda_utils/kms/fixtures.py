import pytest
from os import getenv


@pytest.fixture(scope="session")
def kms_arn() -> str:
    arn = getenv("KMS_ARN")
    if not arn:
        pytest.skip("KMS ARN not found in env vars.")
    return arn
