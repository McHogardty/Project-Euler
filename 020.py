#
# Problem 20 - Factorial digit sum
#
# Find the sum of the digits of 100! = 100 * 99 * 98 * 97 * ...
#


def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n - 1)


def main():
    print(sum(int(x) for x in str(factorial(100))))


if __name__ == "__main__":
    main()
