neigh = [[-1, 0], [0, 1], [1, 0], [0, -1]]

with open('6.in') as file:
    grid = [list(line[:-1]) for line in file]
m, n = len(grid), len(grid[0])

for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == '^':
            start = (i, j)
            break
    else:
        continue
    break


def traverse(edit):
    (i, j), dir = start, 0
    seen = set()
    while 0 <= i < m and 0 <= j < n:
        if (i, j, dir) in seen:
            return True
        seen.add((i, j, dir))
        if edit:
            grid[i][j] = 's'

        ii, jj = i + neigh[dir][0], j + neigh[dir][1]
        if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '#':
            dir = (dir + 1) & 3
        else:
            i, j = ii, jj

    return False


traverse(True)
print(sum(line.count('s') for line in grid))

ret = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 's':
            grid[i][j] = '#'
            if traverse(False):
                ret += 1
            grid[i][j] = 's'
print(ret)
