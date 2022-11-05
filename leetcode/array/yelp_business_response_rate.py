"""Business Messaging Response Rate

On Yelp, users can initiate and engage in private conversations with busness owners. We want to display how responsive a 
business owner is to users that messsage them. To calculate the response rate of a business, we use the following formula, 
expressing the response rate as an integer percentage:

    ```
    floor((num_conversations_with_responses / total_conversations_for_business) * 100)
    ```

Only users can initiate conversations.

Given a business owner ID and a list of messages sent via Yelp, return the given business owner's response rate.
"""
import math


class Message:
    def __init__(self, sender, recipient, conversation_id):
        self.sender = sender
        self.recipient = recipient
        self.conversation_id = conversation_id


def business_responsiveness_rate(biz_owner_id: int, all_messages: list[Message]) -> int:
    """Calculate business response rate

    Calculate the rate at which a business responds to conversations. The rate is an integer percentage of the
    conversations responded to that a business is involved in. Messages that the business is not involved in
    will be ignored.

    Args:
        `biz_owner_id`: the integer ID for the business.
        `all_messages`: A list of `Messages` the business is involved in.

    Returns:
        The response rate as an integer percentage.

    Example:

        ```
        biz_owner_id: 42
        all_messages: [
            Message(**{"sender": 1,  "recipient": 42, "conversation_id": 1}),
            Message(**{"sender": 42, "recipient": 1,  "conversation_id": 1}),
            Message(**{"sender": 2,  "recipient": 42, "conversation_id": 2}),
            Message(**{"sender": 2,  "recipient": 42, "conversation_id": 2}),
            Message(**{"sender": 3,  "recipient": 88, "conversation_id": 3}),
            Message(**{"sender": 3,  "recipient": 42, "conversation_id": 4}),
        ]
        assert business_responsiveness_rate(biz_owner_id, all_messages) == 33
        ```

    """
    conversations = set()  # record the `conversation_id`s this business is involved in
    responses = set()  # record the `conversation_id`s this business responded to

    for message in all_messages:
        # Ignore messages that the business is not involved in
        if message.sender == biz_owner_id or message.recipient == biz_owner_id:
            conversations.add(message.conversation_id)

        # Record a response
        if message.sender == biz_owner_id:
            responses.add(message.conversation_id)

    if not conversations:
        response_rate = 0
    else:
        response_rate = math.floor((len(responses) / len(conversations)) * 100)

    return response_rate
