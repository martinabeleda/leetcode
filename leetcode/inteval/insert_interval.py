"""Insert Interval

You are given an array of non-overlapping intervals intervals where 
`intervals[i] = [start_i, end_i]` represent the start and the end of the ith interval and 
intervals is sorted in ascending order by `start_i`. You are also given an interval 
`new_interval = [start, end]` that represents the start and end of another interval.

Insert `new_interval` into intervals such that intervals is still sorted in ascending order by 
`start_i` and intervals still does not have any overlapping intervals (merge overlapping 
intervals if necessary).

Return intervals after the insertion.

Example 1:

```
Input: intervals = [[1, 3],[6, 9]], new_interval = [2, 5]
Output: [[1, 5], [6, 9]]
Example 2:
```

Example 2:

```
Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval = [4, 8]
Output: [[1, 2],[3, 10], [12, 16]]
Explanation: Because the new interval [4, 8] overlaps with [3, 5], [6, 7], [8, 10].
```

Source: [leetcode](https://leetcode.com/problems/insert-interval/)
"""
Interval = list[int]


def insert(intervals: list[Interval], new_interval: Interval) -> list[Interval]:
    """Insert Interval in array of non-overlapping intervals

    Keep ordered records of the intervals that lie either side of `new_interval` and incrementally
    build the middle interval each time we see an example that overlaps with `new_interval.

    Arguments:
        intervals: A list of the original intervals
        new_interval: The interval to insert

    Returns:
        A list of the intervals after insertion
    """
    left = []
    middle = new_interval
    right = []

    for start, end in intervals:
        if new_interval[0] > end:
            left.append([start, end])
        elif new_interval[1] < start:
            right.append([start, end])
        else:
            middle = [
                min(middle[0], start),
                max(middle[1], end),
            ]

    return left + [middle] + right
