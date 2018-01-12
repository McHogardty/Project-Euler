#
# Problem 21 - Amicable numbers.
#
# Evaluate the sum of all the amicable numbers under 10000.
#

from util import divisors


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
