"""Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

You must solve it in `O(n)` time complexity.

Example 1:

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

Example 2:

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```
"""
import heapq


class Solution:
    def find_kth_largest(self, nums: list[int], k: int, approach: str = "heap") -> int:
        """Find Kth Largest Element in Array"""
        return {
            "heap": self.heap(nums, k),
        }[approach]

    def heap(self, nums: list[int], k: int):
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
