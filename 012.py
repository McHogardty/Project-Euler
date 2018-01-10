#
# Problem 12 - Highly divisible triangular number
#
# Find the value of the first triangle number to have over 500 divisors
#

import math


def num_divisors(n):
    """Calculate the number of divisors of a number."""

    sqrt = math.floor(math.sqrt(n))
    num = 0

    for x in range(1, math.floor(sqrt)):
        if n % x == 0:
            num += 1

    if n % sqrt == 0:
        return 2 * num + 1

    return 2 * num


def main():
    i = 2
    n = 1

    while num_divisors(n) <= 500:
        n += i
        i += 1

    print(n)


if __name__ == "__main__":
    main()
