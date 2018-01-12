#
# Problem 24 - Lexicographic permutations.
#
# What is the millionth lexicographic permutation of the digits 1, 2, 3, 4, 5,
# 6, 7, 8 and 9?
#


from util import factorial


def main():
    # We know how to calculate the number of permutations using factorial.
    # Instead of forming every permutation, we just skip them in chunks using
    # factorial calculations.
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    permutation = []
    count = 0

    while digits:
        for i in range(len(digits)):
            permutations = factorial(len(digits) - 1)

            if count + permutations >= 1000000:
                permutation.append(digits[i])
                digits = digits[:i] + digits[i + 1:]
                break

            count += permutations

    print("".join(permutation))


if __name__ == "__main__":
    main()
