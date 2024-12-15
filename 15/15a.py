dr = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def getstart(grid, m, n):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                grid[i][j] = '.'
                return (i, j)


def move(grid, di, dj, pos):
    (i, j), steps = pos, 0
    while grid[ni := i + di][nj := j + dj] not in '#.':
        i, j, steps = ni, nj, steps + 1
    if grid[ni][nj] == '#':
        return pos
    if steps == 0:
        return (ni, nj)
    grid[ni][nj] = 'O'
    grid[pos[0] + di][pos[1] + dj] = '.'
    return (pos[0] + di, pos[1] + dj)


grid = []
with open('15.in') as file:
    for line in file:
        line = line.strip()
        if not line:
            m, n = len(grid), len(grid[0])
            pos = getstart(grid, m, n)
            continue
        elif line[0] == '#':
            grid.append(list(line))
        else:
            for c in line:
                pos = move(grid, *dr[c], pos)

print(sum(
    100 * i + j for i, row in enumerate(grid) for j, c in enumerate(row)
    if c == 'O'
))
