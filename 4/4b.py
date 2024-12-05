ret = 0
with open('4.in') as file:
    grid = [line[:-1] for line in file]

neigh = [(i, j) for i in (-1, 1) for j in (-1, 1)]
m, n = len(grid), len(grid[0])

for i in range(1, m - 1):
    for j in range(1, n - 1):
        if grid[i][j] != 'A':
            continue
        cur = 0
        for di, dj in neigh:
            if ''.join(grid[i + di * l][j + dj * l] for l in (-1, 1)) == 'MS':
                cur += 1
        if cur == 2:
            ret += 1
print(ret)
