from functools import cache

with open('10.in') as file:
    grid = [line.strip() for line in file]

m, n = len(grid), len(grid[0])


@cache
def dp(i, j):
    if grid[i][j] == '9':
        return set([(i, j)])
    ret = set()
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if (
            0 <= ni < m and 0 <= nj < n
        ) and int(grid[ni][nj]) == int(grid[i][j]) + 1:
            ret |= dp(ni, nj)
    return ret


print(sum(
    len(dp(i, j)) for i in range(m) for j in range(n)
    if grid[i][j] == '0'
))
