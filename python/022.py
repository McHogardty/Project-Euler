#
# Problem 22 - Names scores
#
# Calculate the total of all the name scores in the file data/names.txt. The
# name score is the multiple of the alphabetical position of the name in the
# list with the sum of the alphabetical positions of the letters in the name.
#

import string


def name_score(name):
    """Calculate the name score of an uppercase name."""

    return sum(string.ascii_uppercase.index(x) + 1 for x in name)


def main():
    with open("data/names.txt", "r") as namefile:
        names = namefile.read().replace("\"", "").split(",")

    names.sort()
    print(sum((i + 1) * name_score(name) for i, name in enumerate(names)))


if __name__ == "__main__":
    main()
