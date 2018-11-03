#
# Problem 15 - Lattice paths
#
# How many paths are there through a 20 x 20 grid.
#

PATH_COUNTS = {(1, 1): 2}


def path_count(m, n):
    """Calculate the number of paths in an m x n grid.

    Arguments:
    - m: the width of the grid
    - n: the length of the grid

    """

    if (m, n) in PATH_COUNTS:
        return PATH_COUNTS[(m, n)]

    if m == 1 and n > 1:
        answer = 1 + path_count(1, n - 1)
    elif m > 1 and n == 1:
        answer = path_count(m - 1, 1) + 1
    else:
        answer = path_count(m - 1, n) + path_count(m, n - 1)

    PATH_COUNTS[(m, n)] = answer

    return answer


def main():
    # Cache from the bottom up. Much faster.
    for i in range(1, 20):
        path_count(i, i)

    # We use symmetry here. Either we go right or down at the start.
    # If we go right, we traverse a 19 x 20 grid. If we go left, we traverse
    # a 20 x 19 grid. The number of paths through each grid is the same by
    # symmetry.
    print(2 * path_count(19, 20))


if __name__ == "__main__":
    main()
