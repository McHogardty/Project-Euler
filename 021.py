#
# Problem 21 - Amicable numbers.
#
# Evaluate the sum of all the amicable numbers under 10000.
#

import math


def divisors(n, proper=True):
    """Calculate the divisors of n."""

    sqrt = math.floor(math.sqrt(n))
    d = [1]

    if not proper:
        d.append(n)

    if sqrt < 2:
        return d

    for i in range(2, sqrt + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)

    return d


def main():
    sums = {}
    amicable = []

    for n in range(30000):
        sums[n] = sum(divisors(n))

    for n in range(10000):
        if sums[sums[n]] == n and sums[n] != n:
            amicable.append(n)

    print(sum(amicable))


if __name__ == "__main__":
    main()
