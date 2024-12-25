drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
block_drs = [(-1, 0), (-1, 0), (0, -1), (0, -1)]

with open('12.in') as file:
    grid = [list(line.strip()) for line in file]
m, n = len(grid), len(grid[0])
seen = [[0] * n for _ in range(m)]


def inside(i, j):
    return 0 <= i < m and 0 <= j < n


def hasborder(i, j, di, dj):
    x, y = i + di, j + dj
    return not inside(x, y) or grid[x][y] != grid[i][j]


def cellperimeter(i, j):
    p1, p2 = sum(hasborder(i, j, di, dj) for di, dj in drs), 0
    for (di, dj), (dbi, dbj) in zip(drs, block_drs):
        x, y = i + dbi, j + dbj
        if hasborder(i, j, di, dj) and not (
            inside(x, y) and grid[x][y] == grid[i][j]
            and hasborder(x, y, di, dj)
        ):
            p2 += 1
    return p1, p2


def dfs(i, j):
    if seen[i][j]:
        return [0, 0, 0]
    ret = [1, *cellperimeter(i, j)]
    seen[i][j] = 1
    for di, dj in drs:
        x, y = i + di, j + dj
        if inside(x, y) and grid[x][y] == grid[i][j]:
            for pos, val in enumerate(dfs(x, y)):
                ret[pos] += val
    return ret


ret = [0, 0]
for i in range(m):
    for j in range(n):
        cur = dfs(i, j)
        ret[0] += cur[0] * cur[1]
        ret[1] += cur[0] * cur[2]
print(ret)
