from sortedcontainers import SortedList
dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def getstart(grid, m, n, c):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == c:
                return (i, j)


def getdist(grid, starts):
    djset = SortedList([(0, start) for start in starts])
    dist = {start: 0 for start in starts}

    def check_add(d, u):
        if u in dist and (d0 := dist[u]) > d:
            djset.remove((d0, u))
            dist.pop(u)
        if u not in dist:
            dist[u] = d
            djset.add((d, u))

    while djset:
        d, (i, j, dir) = djset.pop(0)
        di, dj = dr[dir]
        ii, jj = i + di, j + dj
        if grid[ii][jj] != '#':
            check_add(d + 1, (ii, jj, dir))
        for newdir in [dir ^ 1, dir ^ 3]:
            check_add(d + 1000, (i, j, newdir))
    return dist


with open('16.in') as file:
    grid = [line.strip() for line in file]
m, n = len(grid), len(grid[0])

start, end = [getstart(grid, m, n, c) for c in 'SE']
dist = getdist(grid, [(*start, 0)])
enddist = min(dist[(*end, dir)] for dir in range(4))
print(enddist)
