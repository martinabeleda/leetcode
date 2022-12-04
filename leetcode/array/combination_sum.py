"""Combination Sum

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of 
all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return 
the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are 
unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 
150 combinations for the given input.

Example 1:

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

Example 2:

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

Example 3:

```
Input: candidates = [2], target = 1
Output: []
```

Source: [leetcode](https://leetcode.com/problems/combination-sum/)

"""


class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        """Combination Sum

        Approach:
            - Recursive approach. Maintain a stack of the values we're summing up.
            - End condition is if the target is == 0. This means in the previous level, we have all
            of the candidates summed. Keep a list of the solution and add the stack to this list
            - For each of the candidates:
                - If the candidate is greater than the target, skip
                - If the candidate is greater than the last item in the stack, skip. This ensures
                we don't check any duplicate branches since our list of candidates is sorted.
                - If `remainder = 0` then recurse, passing the new target and appending to the
                stack.

        Args:
            candidates: a list of the candidate integers
            target: the integer target

        Returns:
            A list of sublists where each sublist is the combination of candidates that hit the
            target sum.
        ```
        """
        solution = []
        candidates.sort()

        def dfs(candidates: list[int], target: int, stack: list[int]):
            if target == 0:
                solution.append(stack)
                return

            for candidate in candidates:
                if candidate > target:
                    break
                if stack and candidate < stack[-1]:
                    continue
                else:
                    dfs(candidates, target - candidate, stack + [candidate])

        dfs(candidates, target, [])
        return solution
