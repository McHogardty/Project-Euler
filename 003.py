
"""Problem 3 - Largest prime factor

Find the largest prime factor of 600851475143.

"""


def lowest_prime_factor(n):
    """Find the lowest prime factor of n which exceeds 1."""
    if n < 2:
        return n

    for x in range(2, n):
        if n % x == 0:
            # x is the smallest number to divide n, so it must be prime. If it
            # were composite, then it would have a prime factor smaller than
            # x which would thus also be a prime factor of n.
            return x

    return n


def prime_factors(n):
    """Calculate the prime factors of n and return a generator."""
    m = n

    while not m == 1:
        x = lowest_prime_factor(m)
        yield x
        m = m // x


def main():
    print(max(prime_factors(600851475143)))


if __name__ == "__main__":
    main()
