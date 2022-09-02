"""Longest Substring without repeating characters

Given a string `s`, find the length of the longest substring without repeating characters.

Example 1:

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Example 2:

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

Constraints:

- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

Source: [leetcode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
"""


def length_of_longest_substring(string: str) -> int:
    """
    Given a string `s`, return the length of the longest substring without repeating characters.

    Run a sliding window across the string and move the start position such that the window
    is as wide as the longest substring for this index. This approach yields a time complexity
    of O(n) since we must check each character in the string at least once. Space complexity
    is O(1) constant value since the hashmap is bounded to the number of possible characters.

    Arguments:
        string: The string to parse

    Returns:
        The length of the longest substring
    """
    seen = {}  # Record the last seen position of each character
    start = 0  # Maintain a pointer to the start of the sliding window
    longest = 0  # Maintain a record of the longes substring so far

    for i, character in enumerate(string):
        if character in seen and start <= seen[character]:
            # If we've seen the character before, slide the start of the window
            # past it's last seen position
            start = seen[character] + 1
        else:
            # If we haven't seen it before, then our substring grows
            longest = max(longest, i - start + 1)

        # Record this character's last seen position
        seen[character] = i

    return longest
