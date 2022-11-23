"""Find Users with Opt In Changes

Given a list of current users and a log of opt-in changes, find the users
that have a change in their opt-in status  
      
Approach:
    - Build a hash map of users keyed by ID
    - Create a new hash map containing all of the changes
    - Iterate through the `OptInChange` list and apply each to the users
    - If there is an opt-in for a user that doesn't exist, create it
"""

from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    opted_in: bool


@dataclass
class OptInChange:
    user_id: int
    action: str


def is_new_user(current_user: Optional[User], opted_in: bool) -> bool:
    """Return `True` if user is a new opted in `User`"""
    return current_user is None and opted_in


def status_changed(current_user: Optional[User], opted_in: bool) -> bool:
    """Return `True` if user status changed"""
    return current_user and opted_in != current_user.opted_in


def process_change_log(opt_in_change_log: list[OptInChange]) -> dict[int, User]:
    """Create the final state of `Users` given a log of opt-in changes"""
    final_users = defaultdict()
    for opt_in_change in opt_in_change_log:
        opted_in = opt_in_change.action == "opt_in"
        final_users[opt_in_change.user_id] = User(opt_in_change.user_id, opted_in=opted_in)
    return final_users


def find_changed_user_ids(
    current_users: dict[int, User],
    final_users: dict[int, User],
) -> list[int]:
    """Given initial and final user states, return the users that changed their opt-in status"""
    result = []
    for user_id, user in final_users.items():
        current_user = current_users.get(user_id)
        if is_new_user(current_user, user.opted_in) or status_changed(current_user, user.opted_in):
            result.append(user_id)
    return result


def find_users_with_opt_change(
    current_user_list: list[User],
    opt_in_change_log: list[OptInChange],
) -> list[int]:
    """Find users with opt-in changes

    Args:
        current_user_list: list of current `User`s
        opt_in_change_log: a log of opt in changes to be applied

    Returns:
        A list of user IDs that have had their opt-in status changed, sorted by user ID.
    """
    current_users = {user.id: user for user in current_user_list}
    final_users = process_change_log(opt_in_change_log)
    result = find_changed_user_ids(current_users, final_users)
    return sorted(result)
