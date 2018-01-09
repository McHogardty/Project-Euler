
"""Problem 2 - Even Fibonacci numbers

Find the sum of the even valued Fibonacci numbers not exceeding four million.

"""


def fibonacci_sequence(maximum):
    x = 0
    y = 1

    while y < maximum:
        yield y

        x, y = y, x + y


def main():
    total = sum(x for x in fibonacci_sequence(4000000) if x % 2 == 0)

    print(total)


if __name__ == "__main__":
    main()
