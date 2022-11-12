import pytest

from leetcode.array.user_opt_in_changes import (
    OptInChange,
    User,
    find_users_with_opt_change,
)


def test_find_users_with_opt_in_changes():
    current_user_list = [
        User(id=1, opted_in=False),
        User(id=19, opted_in=True),
        User(id=4, opted_in=True),
        User(id=54, opted_in=False),
    ]
    opt_in_change_log = [
        OptInChange(user_id=19, action="opt_out"),
        OptInChange(user_id=1, action="opt_in"),
        OptInChange(user_id=71, action="opt_in"),
        OptInChange(user_id=19, action="opt_in"),
    ]
    assert find_users_with_opt_change(current_user_list, opt_in_change_log) == [1, 71]
