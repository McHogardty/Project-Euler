#
# Problem 10 - Summation of primes
#
# Find the sum of all the primes below 2 million.
#

import math


def is_prime(n):
    """Determine whether or not n is prime."""

    return all(n % x != 0 for x in range(2, math.floor(math.sqrt(n)) + 1))


def main():
    primes = []

    # for n in range(2, 2000000):
    #     if is_prime(n):
    #         primes.append(n)

    # print(primes[:20])
    # print(sum(primes))
    print(sum(n for n in range(2, 2000000) if is_prime(n)))


if __name__ == "__main__":
    main()
