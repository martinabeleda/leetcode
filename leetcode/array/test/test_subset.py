import pytest

from leetcode.array.subset import Solution

TEST_CASES = [
    [
        [4, 1, 0],
        [[], [4], [1], [1, 4], [0], [0, 4], [0, 1], [0, 1, 4]],
    ],
    [
        [1, 2, 3],
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
    ],
    [
        [0],
        [[], [0]],
    ],
    [
        [],
        [[]],
    ],
]


@pytest.mark.parametrize("nums,expected", TEST_CASES)
def test_subset(nums: list[int], expected: list[list[int]]):
    assert sort_result(Solution().subsets(nums)) == sort_result(expected)


def sort_result(result: list[list[int]]):
    return sorted([sorted(r) for r in result])
