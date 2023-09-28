#!/usr/bin/python3
""" Island Perimeter
"""



def island_perimeter(grid):
    """A function that returns the perimeter
    of an island
    """
    peri = 0
    if not grid:
        return peri

    cols, rows = len(grid[0]), len(grid)

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                # Initialize with 4 sides
                peri += 4

                if x > 0 and grid[x - 1][y] == 1:
                    peri -= 1
                if x < rows - 1 and grid[x + 1][y] == 1:
                    peri -= 1
                if y > 0 and grid[x][y - 1] == 1:
                    peri -= 1
                if y < cols - 1 and grid[x][y + 1] == 1:
                    peri -= 1

    return peri
