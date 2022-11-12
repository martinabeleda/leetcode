import pytest

from leetcode.array.destination_city import destination_city


@pytest.mark.parametrize(
    "paths,expected",
    [
        (
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
            "Sao Paolo",
        ),
        ([["B", "C"], ["D", "B"], ["C", "A"]], "A"),
        ([["A", "Z"]], "Z"),
    ],
)
def test_destination_city(paths: list[tuple[str, str]], expected: str):
    assert destination_city(paths) == expected
