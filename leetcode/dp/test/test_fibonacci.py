from leetcode.dp.fibonacci import Solution, Approach

import pytest

APPROACHES = [a for a in Approach]


@pytest.mark.parametrize("approach", APPROACHES)
@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (5, 5),
        (11, 89),
    ],
)
def test_fibonacci(n, expected, approach):
    assert Solution().fib(n, approach) == expected
