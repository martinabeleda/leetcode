"""Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change 
it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after 
performing the above operations.

Example 1:

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

Example 2:

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

Source: 
- [leetcode](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [python solution](https://leetcode.com/problems/longest-repeating-character-replacement/discuss/765776/Python%3A-Two-Pointers-%2B-Process-for-coding-interviews)
"""  # noqa: E501
from collections import Counter


class Solution:
    def character_replacement(self, string: str, k: int) -> int:
        """Longest Repeating Character Replacement

        Approach:
        - Scan the list with a sliding window. Maintain `left` and `right` pointers
        - Store the frequency of each character in the window.
        - Compute the replacement cost: `window_size - highest_frequency`.
            - If `replacement_cost <= k` update the longest string size
            - If `replacement_cost > k` move the window up one index and remove that
            character from the frequency counter. We can slide the entire window since we know
            this is the max length we need to "beat"

        Analysis:
            Time complexity: O(n)
            Space complexity: O(26) = O(1)

        Args:
            string: The string of characters
            k: The number of change operations allowed

        Returns:
            An integer representing the maximum length of repeating characters with replacement
        """
        left = 0
        frequencies = Counter()
        longest_substring = 0

        for right in range(len(string)):
            # Add the new character to the counter
            frequencies.update(string[right])

            # Compute replacement cost
            window_size = right - left + 1
            replacement_cost = window_size - frequencies.most_common()[0][1]
            if replacement_cost <= k:
                longest_substring = window_size
            else:
                frequencies.subtract(string[left])
                left += 1

        return longest_substring
