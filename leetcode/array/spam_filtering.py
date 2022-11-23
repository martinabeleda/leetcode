"""Spam filtering

Given a list of entries of type `{"from": User, "to": User, "message": Text}` create a 
leaderboard of users who received the most number of messages.

Followup. Add a way of filtering spam messages (multiple messages from one user to 
another of the same text)

Assumptions:
    - Assume that a message is only considered as spam if it comes from the same 
        direction. So two users can send the same message without detection.
    - Assume that we only consider a duplicate message as spam if it is sent from
        one user to the same other user. So one user can send the same message to 
        two different users.

Approach:
    - For the first part, we can maintain a hash map where the key is the recipient
        and the value is a counter counting the number of messages received
    - To filter spam:
        - We can create another map that is keyed by "{sender}:{receiver}"  
        - Each key is a "conversation ID" assuming that each user has a unique ID.
            Note that this conversation ID is uni-directional. So it will only 
            contain the messages sent from one user to a different (stable) user.
        - Each value of the map is a set containing the messages. Lookups in the 
            message set are O(1) in the normal case.

"""
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Message:
    sender: int
    recipient: int
    message: str


def user_leaderboard(messages: list[Message]) -> dict[str, int]:
    """Return a leaderboard of users that reveived the most messages

    Args:
        - messages: A list of messages from one user to another

    Returns:
        A dictionary where the key is a user name and the value is the
            number of messages they received
    """
    spam_map = defaultdict(set)
    leaderboard = defaultdict(int)

    for message in messages:
        conversation_key = f"{message.sender}:{message.recipient}"
        if message.message not in spam_map[conversation_key]:
            spam_map[conversation_key].add(message.message)
            leaderboard[message.recipient] += 1

    return leaderboard
