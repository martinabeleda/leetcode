import pytest

from leetcode.heap.kth_largest_element import Solution

TEST_CASES = [
    [[3, 2, 1, 5, 6, 4], 2, 5],
    [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4],
    [[3, 2, 1, 5, 6, 4], 2, 5],
]


@pytest.mark.parametrize("nums,k,expected", TEST_CASES)
@pytest.mark.parametrize("approach", ["heap"])
def test_kth_largest_element(nums: list[int], k: int, expected: int, approach: str):
    assert Solution().find_kth_largest(nums, k, approach) == expected
