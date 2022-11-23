from leetcode.array.yelp_business_response_rate import (
    business_responsiveness_rate,
    Message,
)


def test_business_responsiveness_rate():
    biz_owner_id = 42
    all_messages = [
        Message(**{"sender": 1, "recipient": 42, "conversation_id": 1}),
        Message(**{"sender": 42, "recipient": 1, "conversation_id": 1}),
        Message(**{"sender": 2, "recipient": 42, "conversation_id": 2}),
        Message(**{"sender": 2, "recipient": 42, "conversation_id": 2}),
        Message(**{"sender": 3, "recipient": 88, "conversation_id": 3}),
        Message(**{"sender": 3, "recipient": 42, "conversation_id": 4}),
    ]
    assert business_responsiveness_rate(biz_owner_id, all_messages) == 33
