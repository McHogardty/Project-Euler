#
# Problem 18 - Maximum path sum I
#
# Find the maximum total of any path sum down the following triangle:
#

TRIANGLE = ["75",
            "95 64",
            "17 47 82",
            "18 35 87 10",
            "20 04 82 47 65",
            "19 01 23 75 03 34",
            "88 02 77 73 07 63 67",
            "99 65 04 28 06 16 70 92",
            "41 41 26 56 83 40 80 70 33",
            "41 48 72 33 47 32 37 16 94 29",
            "53 71 44 65 25 43 91 52 97 51 14",
            "70 11 33 28 77 73 17 78 39 68 17 57",
            "91 71 52 38 17 14 91 43 58 50 27 29 48",
            "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
            "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]


def main():
    # Take a number in the second-last row. If that number is on the maximum
    # path, then there are only two choices for the final row. The maximum path
    # will contain the maximum of those two numbers.
    # So we can reduce the final two rows to a single row, summing each number
    # in the second last row with the maximum of the two numbers below it.
    # We keep on applying this procedure until there is a single row left, and
    # then we have the maximum path sum.

    for i in range(len(TRIANGLE)):
        TRIANGLE[i] = [int(x) for x in TRIANGLE[i].split()]

    for n in range(len(TRIANGLE[:-1])):
        for i in range(len(TRIANGLE[-2 - n])):
            TRIANGLE[-2 - n][i] += \
                max(TRIANGLE[-1 - n][i], TRIANGLE[-1 - n][i + 1])

    print(TRIANGLE[0][0])


if __name__ == "__main__":
    main()
