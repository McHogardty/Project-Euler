
"""Problem 1 - Multiples of 3 and 5.

Find the sum of all the multiples of 3 and 5 below 1000."""


def main():
    total = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)

    print(total)


if __name__ == "__main__":
    main()
