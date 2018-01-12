#
# Problem 2 - Even Fibonacci numbers
#
# Find the sum of the even valued Fibonacci numbers not exceeding four million.
#

from util import fibonacci


def main():
    total = sum(x for x in fibonacci(maximum=4000000) if x % 2 == 0)

    print(total)


if __name__ == "__main__":
    main()
