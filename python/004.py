#
# Problem 4 - Largest palindrome product.
#
# Find the largest palindrome made from the product of two 3 digit numbers.
#


import itertools


def is_palindrome(n):
    """Determine whether or not n is a palindrome."""

    n = str(n)

    return all(n[i] == n[len(n) - i - 1] for i in range(len(n) // 2))


def main():
    palindromes = [x * y for x, y in
                   itertools.product(range(100, 1000), range(100, 1000))
                   if is_palindrome(x * y)]

    print(max(palindromes))


if __name__ == "__main__":
    main()
