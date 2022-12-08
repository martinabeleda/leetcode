"""Fibonacci number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
    such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```

Approach:
    - Recursive approach
        - Base cases F(0) and F(1) return 0 and 1 respectively
        - For all other cases, return `F(n - 1) + F(n - 2)`
    - Memoization
        - Allocate an array `memo` to store results as we've calculated them.
        - If we see a solution that we've already calculated (if memo[n] isn't None)
            Then use the solution we've memoized
        - If we haven't seen the solution before, compute it with the fibonacci 
            equation.
"""
from enum import Enum, auto


class Approach(Enum):
    recursive = auto()
    memoize = auto()
    bottom_up = auto()


class Solution:
    def fib(self, n: int, approach: Approach = Approach.bottom_up) -> int:
        callable_map = {
            Approach.recursive: self.fib_recursive,
            Approach.memoize: self.fib_memoize,
            Approach.bottom_up: self.fib_bottom_up,
        }
        return callable_map[approach](n)

    def fib_bottom_up(self, n: int) -> int:
        """Fibonacci sequence using DP bottom up approach"""
        if n == 0:
            return 0
        elif n == 1:
            return 1

        arr = [None] * (n + 1)
        arr[0], arr[1] = 0, 1
        for i in range(2, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
            print(f"{i=}, {arr}")
        return arr[n]

    def fib_memoize(self, n: int) -> int:
        """Fibonacci with memoized solution"""
        memo = [None] * (n + 1)
        return self._fib_memoize(n, memo)

    def _fib_memoize(self, n: int, memo: list[int]) -> int:
        if memo[n]:
            return memo[n]
        elif n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = self._fib_memoize(n - 1, memo) + self._fib_memoize(n - 2, memo)
        memo[n] = result
        return result

    def fib_recursive(self, n: int) -> int:
        """Fibonacci recursive solution"""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)
