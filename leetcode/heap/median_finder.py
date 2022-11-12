"""Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for `arr = [2, 3, 4]`, the median is 3.
For example, for `arr = [2, 3]`, the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `add_num(num: int)` adds the integer num from the data stream to the data structure.
-  `find_median()` returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Approach:
    - Maintain two heaps which represent the two halves of the stream
    - One contains the largest numbers, the other contains the smallest numbers
    - When we get a new number:
        - Add the larger of the new number and the largest in the small heap to the large heap
        - Balance the heaps. We keep len(small heap) > len(large heap)
    - To find the median, handle the even and odd cases:
        - Since we keep the smaller half larger, we can pop the larges number off that list
        - When the heaps are equal, we average the pop values from each

Notes:
    - Heapq supports priority queues where pop returns the smallest value.
    - To implement a max heap, we inverse all the values in the smaller heap.

Runtime analysis:
    - Heap push insertion worst case is O(log N) in the case where we need to heapify each level
    - Heap pop is O(1)
    - Add num is O(log N)
    - Find median operation is O(1)
"""

from heapq import heappush, heappop, heappushpop


class MedianFinder:
    def __init__(self):
        self.larger = []
        self.smaller = []

    def add_num(self, num: int) -> None:
        num = -heappushpop(self.smaller, -num)
        heappush(self.larger, num)
        if len(self.larger) > len(self.smaller):
            heappush(self.smaller, -heappop(self.larger))

    def find_median(self) -> float:
        if len(self.smaller) != len(self.larger):
            return -self.smaller[0]
        else:
            return (-self.smaller[0] + self.larger[0]) / 2
