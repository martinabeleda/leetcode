from leetcode.interval.merge_intervals import merge


def test_merge_intervals():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    assert merge(intervals) == expected


def test_merge_intervals_equal_overlap():
    intervals = [[1, 4], [4, 5]]
    expected = [[1, 5]]
    assert merge(intervals) == expected


def test_merge_intervals_unordered():
    intervals = [[1, 4], [0, 0]]
    expected = [[0, 0], [1, 4]]
    assert merge(intervals) == expected


def test_merge_intervals_unordered_first():
    intervals = [[1, 4], [0, 4]]
    expected = [[0, 4]]
    assert merge(intervals) == expected
