drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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
    return sum(hasborder(i, j, di, dj) for di, dj in drs)


def dfs(i, j):
    if seen[i][j]:
        return [0, 0]
    ret = [1, cellperimeter(i, j)]
    seen[i][j] = 1
    for di, dj in drs:
        x, y = i + di, j + dj
        if inside(x, y) and grid[x][y] == grid[i][j]:
            a, b = dfs(x, y)
            ret[0] += a
            ret[1] += b
    return ret


print(sum(
    (cur := dfs(i, j))[0] * cur[1]
    for i in range(m) for j in range(n)
))
