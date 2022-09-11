"""Subsets

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

Example 2:

```
Input: nums = [0]
Output: [[],[0]]
```

"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """Subsets

        Approach:
            - Sort nums
            - Recursive solution
            - Inputs: nums, subset
            - Take an input list.
                - Return a solution for each of the nums appended to subset
                - Only return solutions where `num` is greater than `subset[-1]
                - This works if the input list is sorted.

        Worked example:
            Result at each level:
                []
                [1], [2], [3]
                [1, 2], [1, 3], [2, 3]
                [1, 2, 3]

            Layer-by-layer:
                nums = [1, 2, 3], subset=[], solution.extend([[1], [2], [3]])
                    nums = [2, 3], subset=[1], solution.extend([[1, 2], [1, 3]])
                        nums = [3], subset=[1, 2], solution.extend([1, 2, 3])
                        nums = [2], subset=[1, 3], return
                    nums = [1, 3], subset=[2], solution.extend([2, 3])
                        nums = [1], subset = [2, 3], return
                    nums = [1, 2], subset=[3], return
        """
        self.solution = [[]]
        self.dfs(sorted(nums), subset=[])
        return self.solution

    def dfs(self, nums: list[int], subset: list[int]):
        for num in nums:
            if not subset or subset[-1] > num:
                result = subset + [num]
                self.solution.append(result)
                self.dfs(nums=[n for n in nums if n != num], subset=result)
            else:
                return
