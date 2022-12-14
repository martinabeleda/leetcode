
from leetcode.string.longest_substring import length_of_longest_substring
from pytest import mark


@mark.parametrize(
    "string,expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("tmmzuxt", 5),
        ("kljhjjff", 4),
    ],
)
def test_length_of_longest_substring(string: str, expected: int):
    assert length_of_longest_substring(string) == expected
