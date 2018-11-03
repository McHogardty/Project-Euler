#
# Problem 23 - Non-abundant sums
#
# Find the sum of all positive integers which cannot be written as the sum of
# two abundant numbers.
#

from util import divisors


def main():
    # Determine all of the abundant integers in this range.
    # Python sets are much faster for lookups than lists.
    abundant = set(n for n in range(1, 28124) if sum(divisors(n)) > n)

    print(sum(n for n in range(1, 28124) if not
              any(n - i in abundant for i in abundant)))


if __name__ == "__main__":
    main()
