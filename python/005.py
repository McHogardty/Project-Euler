#
# Problem 5 - Smallest multiple.
#
# Find the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20.
#


import math


def main():
    # This is the brute force solution.

    # The numbers 1 to 10 are factors of the numbers from 10 to 20. This means
    # That we only need to check for divisibility by all of these numbers.
    numbers = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

    # The highest posisble answer is 20! = 20 * 19 * 18 * ...
    for n in range(20, math.factorial(20), 20):
        if all(n % x == 0 for x in numbers):
            print(n)
            return


if __name__ == "__main__":
    main()
