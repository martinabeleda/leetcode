"""Two Sum

Given an array of integers `nums` and and integer `target`, return indices of the two numbers 
such that they add up to the target

You may assume that each input would have exactly one solution, and you may not use the same 
element twice.

You can return the answer in any order.

Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

Example 3:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

"""


def two_sum(nums: list[int], target: int, approach: str = "optimized") -> list[int]:
    """Return indices of the two numbers in `num` that add up to `target`

    Args:
        nums: a list of the numbers to consider
        target: the target that the result indices should sum to

    Returns:
        A list of the two indices that add up to `target`
    """
    func = {
        "naiive": _two_sum_naiive,
        "optimized": _two_sum_optimized,
    }[approach]
    return func(nums, target)


def _two_sum_optimized(nums, target):
    """Optimized solution with O(n) time complexity.

    Iterate once over `nums` and maintain a hashmap of the numbers we've seen. Since we know what
    number we need to "hit" the target `number = target - element` we can check the hashmap if
    we've seen it before.
    """
    # Maintain a hashmap of the elements we've seen before where the key is the number
    # and the value is the index in `nums`
    seen = {}
    for i, element in enumerate(nums):
        if (number := target - element) in seen:
            # We hit the target, fetch the index of the number we need
            return [i, seen[number]]
        else:
            # Record the element we just processed
            seen[element] = i


def _two_sum_naiive(nums, target):
    """Naiive solution with O(n^2) time complexity

    This solution brute forces the problem by checking every combination of values in `nums`.
    We need to add a contition to ignore cases where we're comparing the same indice. Worst-case
    O(n^2) if the solution is the last pair.
    """
    for i, left in enumerate(nums):
        for j, right in enumerate(nums):
            if i == j:
                continue
            if left + right == target:
                return [i, j]
