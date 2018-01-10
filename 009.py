#
# Problem 9 - Special Pythagorean triplet
#
# Find the product of the numbers in the only Pythagorean triplet whose numbers
# sum to 1000.
#


def is_triplet(x, y, z):
    return (x**2 + y**2) == z**2


def main():
    # The brute force calcuation.

    for m in range(1, 999):
        for n in range(1, 1000 - m):
            if m + n > 999:
                continue

            if is_triplet(m, n, 1000 - (m + n)):
                print(m, n, 1000 - (m + n))
                print(m * n * (1000 - (m + n)))
                return


def alternative():
    # Given the constraints, we may calculate the triplet by solving the
    # equation m**2 + n**2 = (1000 - (m + n))**2 for n. Much faster.

    for m in range(1, 999):
        if (500 * ((2 * m) - 1000)) % (m - 1000) == 0:
            n = 500 * ((2 * m) - 1000) // (m - 1000)
            print(m * n * (1000 - m - n))
            return


if __name__ == "__main__":
    # main()
    alternative()
