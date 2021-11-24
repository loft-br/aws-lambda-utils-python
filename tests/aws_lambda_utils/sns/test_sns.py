from mypy_boto3_sns.service_resource import Topic
from aws_lambda_utils.sns.isns import ITopicWrapper
from datetime import datetime


def test_send_text_message(topic_wrapper: ITopicWrapper, phone_number: str):
    message_id = topic_wrapper.publish_sms_message(
        phone_number,
        message=f"Testing sns.publish_text_message at {datetime.now().isoformat()}. Essa mensagem eh do Mago do Python.",
    )
    assert message_id is not None


def test_publish_message(topic_wrapper: ITopicWrapper):
    message_id = topic_wrapper.publish_message("Testing message")
    assert message_id is not None


def test_publish_multi_message(topic_wrapper: ITopicWrapper):
    message_id = topic_wrapper.publish_multi_message(
        "Demo subject",
        default_message="Demo default message",
        sms_message="Demo sms message",
        email_message="<span>Demo Email messsage<span>",
    )

    assert message_id is not None
