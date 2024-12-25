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
enddist, D = dist[end[0]][end[1]], 100


def count(delta, D):
    ret = 0
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == '#':
                continue
            for x in range(max(1, i - delta), min(m - 1, i + delta + 1)):
                deltay = delta - abs(x - i)
                for y in range(max(1, j - deltay), min(n - 1, j + deltay + 1)):
                    if grid[x][y] != '#' and (
                        dist[i][j] + revdist[x][y] + abs(x - i) + abs(y - j)
                        <= enddist - D
                    ):
                        ret += 1
    return ret


print(count(2, 100), count(20, 100))
