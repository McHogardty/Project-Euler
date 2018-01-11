#
# Problem 14 - Longest Collatz sequence
#
# Find the longest Collatz sequence with a starting number under 1 million.
#


# Keep track of the calculated sequences.
# COLLATZ[i] contains the length of the sequence starting at i + 1.
COLLATZ = {1: 1}


def collatz_length(n):
    """Calculate the Collatz sequence starting at n as a generator."""

    if n in COLLATZ:
        return COLLATZ[n]

    if n % 2 == 0:
        COLLATZ[n] = collatz_length(n // 2) + 1
    else:
        COLLATZ[n] = collatz_length((3 * n) + 1) + 1

    return COLLATZ[n]


def main():
    longest = 1
    answer = 1

    for n in range(1, 1000000):
        x = collatz_length(n)
        if x > longest:
            answer = n
            longest = x

    print(answer)


if __name__ == "__main__":
    main()
