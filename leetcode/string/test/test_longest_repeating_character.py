from leetcode.string.longest_repeating_character import Solution
import pytest


@pytest.mark.parametrize(
    "string,k,expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("BAAAABBA", 1, 5),
        ("BAAAABBA", 3, 8),
        ("BAAAABBBBBA", 1, 6),
        ("CBAAAABBBBBA", 2, 7),
        ("CBAAAABBBBBA", 1, 6),
        ("CABAAAABBBBBA", 2, 7),
        ("", 1, 0),
        ("AAAA", 3, 4),
        ("AAAA", 1, 4),
    ],
)
def test_longest_repeating_character(string, k, expected):
    assert Solution().character_replacement(string, k) == expected
