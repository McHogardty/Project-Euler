#
# Problem 10 - Summation of primes
#
# Find the sum of all the primes below 2 million.
#

from util import is_prime


def main():
    print(sum(n for n in range(2, 2000000) if is_prime(n)))


if __name__ == "__main__":
    main()
