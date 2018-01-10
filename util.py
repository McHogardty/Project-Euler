"""Useful functions for solving the Project Euler problems."""

import math


def is_prime(n):
    """Determine whether or not n is prime."""

    if n < 2:
        # A prime number is positive and has only 2 factors. 1 has one factor.
        return False

    return all(n % x != 0 for x in range(2, math.floor(math.sqrt(n)) + 1))
