#
# Problem 30 - Digit fifth powers
#
# Find the sum of all of the numbers which can be written as the sum of the
# fifth powers of their digits.
#


def main():
    # Dictionary lookups are O(1) and cheaper than calculating the power all
    # the time for 1000000 numbers.
    powers = {str(n): n**5 for n in range(10)}
    numbers = []

    # The upper bound is calculated by figuring out when 9^5 * n < -1 + 10^n.
    # So we solve 59049n + 1 < 10^n, giving is n ~ 5.2. So this occurs when
    # n > 5.2 = 6.
    for n in range(10, 1000000):
        if sum(powers[x] for x in str(n)) == n:
            numbers.append(n)

    print(sum(numbers))


if __name__ == "__main__":
    main()
