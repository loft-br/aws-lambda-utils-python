import pytest
from os import getenv
import logging

pytest_plugins = [
    "tests.aws_lambda_utils.sns.fixtures",
    "tests.aws_lambda_utils.kms.fixtures",
]

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


@pytest.fixture(scope="session")
def phone_number() -> str:
    phone_number = getenv("PHONE_NUMBER")
    if not phone_number:
        pytest.skip("Phone number not found in env vars.")
    return phone_number


@pytest.fixture(scope="session")
def email() -> str:
    email = getenv("EMAIL")
    if not email:
        pytest.skip("Email not found in env vars.")
    return email
