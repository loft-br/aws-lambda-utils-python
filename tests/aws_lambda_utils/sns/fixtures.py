from typing import Any, Iterable
import boto3
from mypy_boto3_sns.service_resource import Subscription, Topic
import pytest
from aws_lambda_utils.sns.isns import ITopicWrapper
from aws_lambda_utils.sns.sns import TopicWrapper
import time

TOPIC_NAME_PREFIX = "demo-basics-topic"


@pytest.fixture(scope="session")
def topic_name() -> str:
    return f"{TOPIC_NAME_PREFIX}-{time.time_ns()}"


@pytest.fixture(scope="session")
def aws_topic(topic_name: str) -> Iterable[Topic]:
    aws_topic = boto3.resource("sns").create_topic(Name=topic_name)
    yield aws_topic
    aws_topic.delete()


@pytest.fixture(scope="session")
def topic_wrapper(aws_topic: Topic) -> ITopicWrapper:
    return TopicWrapper(aws_topic.arn)


@pytest.fixture
def email_sub(aws_topic: Topic, email: str) -> Iterable[Subscription]:
    sub = aws_topic.subscribe(Protocol="email", Endpoint=email)
    yield sub
    sub.delete(sub)


@pytest.fixture
def phone_sub(aws_topic: Topic, phone_number: str) -> Iterable[Subscription]:
    sub = aws_topic.subscribe(Protocol="sms", Endpoint=phone_number)
    yield sub
    sub.delete()
