#
# Problem 7 - 10001st prime.
#
# Find the 10001st prime number.
#


from util import is_prime

def main():
    i = 0
    n = 1

    while i < 10001:
        n += 1

        if is_prime(n):
            i += 1

    print(n)


if __name__ == "__main__":
    main()
