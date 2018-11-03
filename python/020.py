#
# Problem 20 - Factorial digit sum
#
# Find the sum of the digits of 100! = 100 * 99 * 98 * 97 * ...
#


from util import factorial


def main():
    print(sum(int(x) for x in str(factorial(100))))


if __name__ == "__main__":
    main()
