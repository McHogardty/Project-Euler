#
# Problem 29 - Distinct powers.
#
# How many distinct terms are formed by the powers a^b with a and b ranging
# between 2 and 100?
#


def main():
    powers = set()

    for a in range(2, 101):
        b = a
        for _ in range(2, 101):
            b *= a
            powers.add(b)

    print(len(powers))


if __name__ == "__main__":
    main()
