from leetcode.interval.insert_interval import insert
from pytest import mark


@mark.parametrize(
    "intervals,new_interval,expected",
    [
        (
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]],
        ),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        (
            [[1, 2], [3, 5], [8, 10]],
            [9, 10],
            [[1, 2], [3, 5], [8, 10]],
        ),
    ],
)
def test_insert(intervals, new_interval, expected):
    assert insert(intervals, new_interval) == expected
