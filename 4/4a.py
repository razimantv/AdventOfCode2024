ret = 0
with open('4.in') as file:
    grid = [line[:-1] for line in file]

neigh = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
m, n = len(grid), len(grid[0])

for i in range(m):
    for j in range(n):
        if grid[i][j] != 'X':
            continue
        for di, dj in neigh:
            for l in range(1, 4):
                ni, nj = i + di * l, j + dj * l
                if not (0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 'XMAS'[l]):
                    break
            else:
                ret += 1
print(ret)
