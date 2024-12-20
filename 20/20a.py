from sortedcontainers import SortedList
dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def getstart(grid, m, n, c):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == c:
                return (i, j)


def getdist(grid, m, n, start):
    todo = [start]
    dist = [[float('inf')] * n for _ in range(m)]
    dist[start[0]][start[1]] = 0

    while todo:
        next = []
        for i, j in todo:
            for di, dj in dr:
                ni, nj = i + di, j + dj
                if grid[ni][nj] != '#' and dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    next.append((ni, nj))
        todo = next
    return dist


with open('20.in') as file:
    grid = [line.strip() for line in file]
m, n = len(grid), len(grid[0])

start, end = [getstart(grid, m, n, c) for c in 'SE']
dist, revdist = getdist(grid, m, n, start), getdist(grid, m, n, end)
enddist, ret, D = dist[end[0]][end[1]], 0, 100
for i in range(1, m - 1):
    for j in range(1, n - 1):
        if grid[i][j] == '#':
            for dx, dy in dr:
                if (
                    dist[i + dx][j + dy] + revdist[i - dx][j - dy] + 2 + D
                    <= enddist
                ):
                    ret += 1
                    break

print(ret)
