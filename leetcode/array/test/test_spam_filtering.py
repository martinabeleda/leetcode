from leetcode.array.spam_filtering import user_leaderboard, Message


def test_user_leaderboard():
    messages = [
        Message(sender=1, recipient=2, message="Hi"),
        Message(sender=2, recipient=1, message="Hello"),
        Message(sender=3, recipient=4, message="Hello"),
        Message(sender=1, recipient=2, message="How's it going?"),
    ]
    expected = {
        1: 1,
        2: 2,
        4: 1,
    }
    result = user_leaderboard(messages)
    assert result == expected


def test_user_leaderboard_with_spam():
    """Test that spam messages are detected when sent from the same user"""
    messages = [
        Message(sender=1, recipient=2, message="hi"),
        Message(sender=1, recipient=2, message="hi"),
        Message(sender=2, recipient=1, message="world"),
        Message(sender=1, recipient=2, message="hello"),
    ]
    expected = {
        2: 2,
        1: 1,
    }
    assert user_leaderboard(messages) == expected


def test_user_leaderboard_spam_one_way():
    """Ensure that a duplicate message is not detected as spam if it is sent by
    different users
    """
    messages = [
        Message(sender=1, recipient=2, message="hi"),
        Message(sender=2, recipient=1, message="hi"),
    ]
    expected = {
        1: 1,
        2: 1,
    }
    assert user_leaderboard(messages) == expected


def test_user_leaderboard_multiple_spam():
    """Ensure that spam is filtered when sent from multiple sources"""
    messages = [
        Message(sender=1, recipient=2, message="hi"),
        Message(sender=1, recipient=2, message="hi"),
        Message(sender=2, recipient=1, message="world"),
        Message(sender=1, recipient=2, message="hello"),
        Message(sender=3, recipient=4, message="foo"),
        Message(sender=3, recipient=4, message="bar"),
        Message(sender=4, recipient=3, message="hello"),
        Message(sender=3, recipient=4, message="bar"),
    ]
    expected = {
        2: 2,
        1: 1,
        3: 1,
        4: 2,
    }
    assert user_leaderboard(messages) == expected
