import pytest

from leetcode.array.destination_city import destination_city, destination_city_set

SOLUTIONS = [destination_city, destination_city_set]


@pytest.mark.parametrize(
    "paths,expected",
    [
        (
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paolo"]],
            "Sao Paolo",
        ),
        ([["B", "C"], ["D", "B"], ["C", "A"]], "A"),
        ([["A", "Z"]], "Z"),
    ],
)
@pytest.mark.parametrize("solution", SOLUTIONS)
def test_destination_city(
    paths: list[tuple[str, str]],
    expected: str,
    solution: callable,
):
    assert solution(paths) == expected
