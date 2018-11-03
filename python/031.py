#
# Problem 31 - Coin sums
#
# How many different ways can 2 pounds me made out pound sterling coins?
#


def combinations(total, options):
    """Calculate the number of combinations available from the given options.

    Assumes that options are sorted in descending order and the total exceeds
    the maximum in options."""

    if not options:
        return 0

    o, remaining = options[0], options[1:]

    if not remaining:
        return int(total % o == 0)

    count = 0
    for n in range(1, (total // o) + 1):
        if n * o == 200:
            count += 1
            break
        for m in range(len(remaining)):
            count += combinations(total - (n * o), remaining[m:])

    return count


def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    count = 0

    for n in range(len(coins)):
        count += combinations(200, coins[n:])

    print(count)


if __name__ == "__main__":
    main()
