#
# Problem 32 - Pandigital products.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#


def main():
    products = set()
    digits = set(("1", "2", "3", "4", "5", "6", "7", "8", "9"))

    # We are limited to digits. A five digit number multiplied by a single
    # digit number will have at least five digits. Hence we must limit
    # ourselves to numbers with at most four digits.
    for n in range(1, 10000):
        s = str(n)

        if "0" in s:
            continue

        if len(set(s)) != len(s):
            continue

        # We have the following restrictions on m:
        # - m is more than n, to prevent us considering the same product twice.
        # - m is restricted by the length of n.  If n is 1 digit, m may be four
        #   digits. If n is 2 digits, m may be at most 3 digits, etc.
        for m in range(n + 1, 10 ** (5 - len(s))):
            t = str(m)

            if "0" in t:
                continue

            if len(set(t)) != len(t):
                continue

            if any(x in t for x in s):
                continue

            remaining = digits.difference(x for x in s + t)

            product = str(m * n)
            product_set = set(product)

            if len(product_set) != len(product):
                continue

            if product_set == remaining:
                products.add(m * n)

    print(sum(products))


if __name__ == "__main__":
    main()
