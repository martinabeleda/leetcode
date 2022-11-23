from typing import List

import pytest

from leetcode.matrix.map_search import possible_moves, is_reachable


@pytest.fixture
def map_a() -> List[List[int]]:
    return [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
    ]


@pytest.mark.parametrize(
    "location,expected",
    [
        ((2, 2), {(1, 2), (2, 1), (2, 3), (3, 2)}),
        ((0, 0), {(1, 0), (0, 1)}),
        ((2, 0), {(1, 0), (2, 1)}),
        ((5, 4), set()),
    ],
)
def test_possible_moves(location, expected, map_a):
    assert possible_moves(map_a, location) == expected


@pytest.fixture
def map_bc() -> List[List[int]]:
    return [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ]


@pytest.mark.parametrize(
    "location,destination,expected",
    [
        ((0, 0), (2, 0), True),
        ((2, 1), (0, 4), True),
        ((2, 1), (4, 1), False),
        ((4, 0), (0, 2), False),
        ((0, 4), (0, 2), True),
    ],
)
def test_possible_moves(location, destination, expected, map_bc):
    assert is_reachable(map_bc, location, destination) == expected
