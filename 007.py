#
# Problem 7 - 10001st prime.
#
# Find the 10001st prime number.
#


import math


def is_prime(n):
    """Determine whether or not n is prime."""

    return all(n % x != 0 for x in range(2, math.floor(math.sqrt(n)) + 1))


def main():
    i = 0
    n = 1

    while i < 10001:
        n += 1

        if is_prime(n):
            i += 1

    print(n)


if __name__ == "__main__":
    main()
