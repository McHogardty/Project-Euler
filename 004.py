
"""Problem 4 - Largest palindrome product.

Find the largest palindrome made from the product of two 3 digit numbers.

"""


import itertools


def is_palindrome(n):
    """Determine whether or not n is a palindrome."""

    n = str(n)

    return not any(n[i] != n[len(n) - i - 1] for i in range(len(n) // 2))


def main():
    numbers = [x * y for x, y in
               itertools.product(range(100, 1000), range(100, 1000))]
    numbers.sort(reverse=True)

    for n in numbers:
        if is_palindrome(n):
            print(n)
            return


if __name__ == "__main__":
    main()
