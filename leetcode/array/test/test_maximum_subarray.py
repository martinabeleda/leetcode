from leetcode.array.maximum_subarray import Solution
import pytest


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
    ],
)
def test_max_subarray(nums, expected):
    assert Solution().max_subarray(nums) == expected
