"""Useful functions for solving the Project Euler problems."""

import math


def is_prime(n):
    """Determine whether or not n is prime."""

    return all(n % x != 0 for x in range(2, math.floor(math.sqrt(n)) + 1))
