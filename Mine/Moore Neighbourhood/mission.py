def count_neighbours(grid, row, col):
    rows = [i for i in range(row - 1, row + 2)]
    cols = [i for i in range(col - 1, col + 2)]
    neighbours = 0
    for r in rows:
        if r < 0 or r > len(grid) - 1:
            pass
        else:
            for c in cols:
                if c < 0 or c > len(grid[0]) - 1:
                    pass
                elif r == row and c == col:
                    pass
                else:
                    if grid[r][c] == 1:
                        neighbours += 1
    return neighbours


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
