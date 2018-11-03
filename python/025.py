#
# Problem 25 - 1000-digit Fibonacci number
#
# What is the index of the first term in the Fibonacci sequence to have 1000
# digits?
#


from util import fibonacci


def main():
    n = 1

    for f in fibonacci():
        if len(str(f)) == 1000:
            print(n)
            break

        n += 1


if __name__ == "__main__":
    main()
