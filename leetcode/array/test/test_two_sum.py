from leetcode.array.two_sum import two_sum
import pytest


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
    ],
)
@pytest.mark.parametrize("approach", ["naiive", "optimized"])
def test_two_sum(nums, target, expected, approach):
    assert set(two_sum(nums, target, approach)) == expected


@pytest.mark.parametrize(
    "nums,target",
    [
        ([2, 7, 11, 15], 100),
        ([3, 2, 4], 10),
        ([3, 3], 9),
    ],
)
@pytest.mark.parametrize("approach", ["naiive", "optimized"])
def test_two_sum_invalid(nums, target, approach):
    assert two_sum(nums, target, approach) is None
