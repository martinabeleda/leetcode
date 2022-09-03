"""Spiral Matrix

Given an `m x n` matrix, return all elements of the matrix in spiral order.

Example 1:

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

Example 2:

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

Source: [leetcode](https://leetcode.com/problems/spiral-matrix/)
"""
from __future__ import annotations

from enum import Enum


class Direction(Enum):
    RIGHT = "RIGHT"
    DOWN = "DOWN"
    LEFT = "LEFT"
    UP = "UP"

    def get_next_direction(self) -> Direction:
        return {
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
            Direction.UP: Direction.RIGHT,
        }[self]

    def get_next_position(self, i: int, j: int) -> tuple[int, int]:
        return {
            Direction.RIGHT: [i + 1, j],
            Direction.DOWN: [i, j + 1],
            Direction.LEFT: [i - 1, j],
            Direction.UP: [i, j - 1],
        }[self]


class SpiralOrder:
    def run(self, matrix: list[list[int]]) -> list[int]:
        """Spiral Order

        Consider a state machine where we initialize the traverse direction. We can continue to
        traverse in our current direction until we hit an end condition. If we're at an end
        condition, we must change the traverse direction in a pre-determined way.

        Now, the question is - how do we define the end condition? Either the next block in our
        desired direction:
            1. Doesn't exist -> Index error
            2. Has already been seen -> Maintain an visitation grid?

        If we hit an end condition then, change the traversal direction in a clockwise direction

        Args:
            matrix: the matrix of numbers to traverse

        Returns:
            A list of the elements visited in order
        """
        # Initial conditions
        i, j = 0, 0  # Start at the top left corner
        direction = Direction.RIGHT  # Start traversing to the right

        self.width, self.height = len(matrix[0]), len(matrix)
        self.create_visitation_grid(self.width, self.height)

        result = []
        while True:
            # Update the result with the current position
            result.append(matrix[j][i])
            self.visitation_grid[j][i] = True

            # Get the next valid position
            next_position = direction.get_next_position(i, j)
            if self.is_occupied(next_position):
                direction = direction.get_next_direction()
                next_position = direction.get_next_position(i, j)
                if self.is_occupied(next_position):
                    return result

            # Set the next index
            i, j = next_position

    def is_occupied(self, position: list[int, int]) -> bool:
        i, j = position

        # Check boundary conditions (based on the matrix shape)
        try:
            self.visitation_grid[j][i]
        except IndexError:
            return True

        # Check if we've visited this point before
        if self.visitation_grid[j][i]:
            return True

        # If we've made it here, position is a free element in the matrix
        return False

    def create_visitation_grid(self, width: int, height: int):
        self.visitation_grid = [[0 for _ in range(width)] for _ in range(height)]
