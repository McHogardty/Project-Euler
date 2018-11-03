#
# Problem 17 - Number letter counts
#
# How many letters would be used to write out the numbers from 1 to 1000?
#

UNITS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]

TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]


def main():
    words = []

    for n in range(1, 1001):
        w, r = divmod(n, 1000)
        if w > 0:
            words.append(UNITS[w])
            words.append("thousand")

        x, r = divmod(r, 100)
        if x > 0:
            words.append(UNITS[x])
            words.append("hundred")

        y, z = divmod(r, 10)
        if y > 0:
            if y == 1:
                words.append(UNITS[r])
            else:
                words.append(TENS[y])
        if z > 0 and y != 1:
            words.append(UNITS[z])

        if (w + x) > 0 and (y + z) > 0:
            words.append("and")

    print(len("".join(words)))


if __name__ == "__main__":
    main()
