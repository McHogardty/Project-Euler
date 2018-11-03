#
# Problem 26 - Reciprocal cycles
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.
#

from util import prime_factors


def main():
    # The period of a repeating decimal is the multiplicative order of 10
    # modulo the denominator, i.e. the lowest number k such that 10**k = 1
    # modulo the denominator.
    # Note that if the prime decomposition of n consists only of 2 and 5, it
    # will be a terminating decimal and can be immediately excluded.
    # Additionally, the period of the repeating decimal is always less than the
    # denominator.

    max_period = 0
    answer = 0

    for n in range(2, 1000):
        if all(x == 2 or x == 5 for x in prime_factors(n)):
            continue

        for k in range(1, n):
            if (10**k) % n == 1:
                if k > max_period:
                    answer = n
                    max_period = k
                break

    print(answer)


if __name__ == "__main__":
    main()
