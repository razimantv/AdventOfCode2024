from functools import cache

with open('10.in') as file:
    grid = [[int(x) for x in line.strip()] for line in file]
m, n = len(grid), len(grid[0])


@cache
def dp(i, j):
    if grid[i][j] == 9:
        return set([(i, j)]), 1
    unique, cnt = set(), 0
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[i][j] + 1:
            unique |= (child := dp(ni, nj))[0]
            cnt += child[1]
    return unique, cnt


print(sum(
    len(dp(i, j)[0]) for i in range(m) for j in range(n)
    if grid[i][j] == 0
))
print(sum(
    dp(i, j)[1] for i in range(m) for j in range(n)
    if grid[i][j] == 0
))
