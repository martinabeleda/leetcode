"""Map Search

**Part A**

Find the adjacent positions you can move to given a location on the map below:


    1 = wall (cannot move to this position)
    0 = not wall (can move to this position)
    
    For example, an input of (2,3) means that you will be determining the possible moves at 
    location “row 2” and “column 3”. The index of the input starts at 0


**Part B**

Determine if you can reach the destination from a given location on the map.

"""
from typing import List, Tuple, Set
from copy import deepcopy


def possible_moves(map: List[List[int]], location: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """Find the adjacent positions you can move to given a location on the map"""
    y, x = location
    moves = [
        (y - 1, x),
        (y + 1, x),
        (y, x - 1),
        (y, x + 1),
    ]
    result = set()
    for move in moves:
        next_y = move[0]
        next_x = move[1]

        # Check the boundary conditions
        if (next_y < 0) or (next_x < 0):
            continue
        if (next_y >= len(map)) or (next_x >= len(map[0])):
            continue

        if map[next_y][next_x] == 0:
            result.add(move)

    return result


def is_reachable(
    map: List[List[int]],
    current_location: Tuple[int, int],
    destination: Tuple[int, int],
) -> bool:
    """Determine if you can reach the destination from a given location

    Approach:
        - depth first search.
        - search over all possible moves until we can't anymore.
        - check if the destination is in those
        - we use the same map to store visitation
    """
    visited = deepcopy(map)
    return _is_reachable(visited, current_location, destination)


def _is_reachable(
    map: List[List[int]],
    current_location: Tuple[int, int],
    destination: Tuple[int, int],
) -> bool:
    next_locations = possible_moves(map, current_location)
    for next_location in next_locations:
        if next_location == destination:
            return True

    map[current_location[0]][current_location[1]] = 1
    return any(is_reachable(map, l, destination) for l in next_locations)  # noqa: E741
