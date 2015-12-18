with open("inputs/day18.txt", "r") as file:
    data = file.readlines()

n = len(data)
grid = [[True if c == '#' else False for c in s] for s in data]
mode = 'part1'


def brokenGrid(grid):
    grid[0][0] = True
    grid[0][n - 1] = True
    grid[n - 1][0] = True
    grid[n - 1][n - 1] = True


def neighboursInLine(line, i):
    x = 0
    if i > 0:
        x += 1 if line[i - 1] else 0
    x += 1 if line[i] else 0
    if i < n - 1:
        x += 1 if line[i + 1] else 0
    return x


def neighbours(grid, i, j):
    x = 0

    if i > 0:
        x += neighboursInLine(grid[i - 1], j)

    x += neighboursInLine(grid[i], j)
    if grid[i][j]:
        x -= 1

    if i < n - 1:
        x += neighboursInLine(grid[i + 1], j)

    return x


def nextGrid(grid):
    next = [[False] * n for j in range(n)]

    for i in range(n):
        for j in range(n):
            x = neighbours(grid, i, j)
            if grid[i][j]:
                next[i][j] = (x == 2 or x == 3)
            else:
                next[i][j] = (x == 3)
    return next


for i in range(100):
    grid = nextGrid(grid)

on = sum(map(sum, grid))

print('Part 1', on)

grid = [[True if c == '#' else False for c in s] for s in data]
brokenGrid(grid)

for i in range(100):
    grid = nextGrid(grid)
    brokenGrid(grid)

on = sum(map(sum, grid))

print('Part 2', on)
