#
# Problem 27 - Quadratic primes.
#
# Find the product of the coefficients of the linear and constant terms of the
# monic quadratic polynomial in n which produces the maximum number of primes
# for consecutive values of n, starting at n = 0.
#

from util import is_prime


def quadratic(a, b):
    def q(n):
        return n * n + a * n + b

    return q


def main():
    # Note that the constant term of the quadratic must be prime, because
    # when n = 0 it equals the constant term.
    # Also note that when n equals the constant term, every term will be
    # divisible by n and our list of primes terminates.
    answer = 0
    max_primes = 0
    primes = set(x for x in range(1000) if is_prime(x))

    for b in primes:
        for a in range(1, 1000):
            for a, b in ((a, b), (a, -b), (-a, b), (-a, -b)):
                q = quadratic(a, b)

                n = 0
                while q(n) in primes:
                    n += 1

                if n > max_primes:
                    answer = a * b
                    max_primes = n

    print(answer)


if __name__ == "__main__":
    main()
