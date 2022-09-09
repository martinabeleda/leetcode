from leetcode.array.combination_sum import Solution
import pytest


@pytest.mark.parametrize(
    "candidates,target,expected",
    [
        (
            [2, 3, 6, 7],
            7,
            [[2, 2, 3], [7]],
        ),
        (
            [2, 3, 5],
            8,
            [[3, 5], [2, 2, 2, 2], [2, 3, 3]],
        ),
        (
            [2],
            1,
            [],
        ),
        (
            [1],
            1,
            [[1]],
        ),
    ],
)
def test_combination_sum(candidates, target, expected):
    result = Solution().combination_sum(candidates, target)
    assert sorted([sorted(r) for r in result]) == sorted([sorted(e) for e in expected])
