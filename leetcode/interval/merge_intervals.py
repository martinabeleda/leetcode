"""Merge Intervals

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping
intervals, and return an array of the overlapping intervals that cover all the intervals in
the input.

Approach:
    - Iterate once over the intervals
    - Store the current interval start and end
    - Get the next interval
        - If the next interval start is `<=` the end of the current, merge.
            - End is next interval end.
        - Else, continue
            - Append current interval to result

Example:
    `intervals = [[1,3],[2,6],[8,10],[15,18]]`
    first
        start = 1, end = 3
        start_n = 2, end_n = 6
        2 <= 3, merge
    
    second
        start = 1, end = 6
        start_n = 8, end_n = 10
        8 !<= 6
        continue
    
    third
        start = 8, end = 10
        start_n = 15, end_n = 18
        15 !<= 10
        continue
        
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    start, end = intervals[0]
    for next_start, next_end in intervals[1:]:
        if next_start <= end:
            end = max(end, next_end)
        else:
            result.append([start, end])
            start, end = next_start, next_end
    result.append([start, end])
    return result
