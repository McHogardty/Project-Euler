"""Useful functions for solving the Project Euler problems."""

from math import floor, sqrt


def divisors(n, proper=True):
    """Calculate the divisors of n."""

    sq = floor(sqrt(n))
    d = [1]

    if not proper:
        d.append(n)

    if sq < 2:
        return d

    for i in range(2, sq + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)

    if sq * sq == n:
        # We will have a duplicate.
        return d[:-1]

    return d


def factorial(n):
    """Calculate n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1. By convention,
    1! = 1 and 0! = 1.

    """

    if n < 2:
        return 1

    return n * factorial(n - 1)


def fibonacci(maximum=None):
    """Calculate the Fibonacci sequence and return it as a generator."""
    x = 0
    y = 1

    while True:
        yield y

        x, y = y, x + y

        if maximum is not None and y > maximum:
            return


def is_prime(n):
    """Determine whether or not n is prime."""

    if n < 2:
        # A prime number is positive and has only 2 factors. 1 has one factor.
        return False

    return all(n % x != 0 for x in range(2, floor(sqrt(n)) + 1))
