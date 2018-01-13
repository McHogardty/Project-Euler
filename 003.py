#
# Problem 3 - Largest prime factor
#
# Find the largest prime factor of 600851475143.
#


from util import prime_factors


def main():
    print(max(prime_factors(600851475143)))


if __name__ == "__main__":
    main()
