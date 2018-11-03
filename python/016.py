#
# Problem 16 - Power digit sum
#
# What is the sum of the digits of 2^1000?
#


def main():
    print(sum(int(x) for x in str(2**1000)))


if __name__ == "__main__":
    main()
