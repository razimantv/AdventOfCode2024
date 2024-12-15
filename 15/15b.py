import queue

dr = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
double = {'#':  '##', '.': '..', 'O': '[]', '@': '@.'}


def getstart(grid, m, n):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                grid[i][j] = '.'
                return (i, j)


def move(grid, di, dj, pos):
    bfsq = queue.Queue()
    bfsq.put((pos[0], pos[1], '.'))
    todo = [(pos[0], pos[1], '.')]
    grid[pos[0]][pos[1]] = '@'
    while not bfsq.empty():
        i, j, c = bfsq.get()
        ni, nj = i + di, j + dj
        if grid[ni][nj] == '#':
            break
        elif grid[ni][nj] in '[]':
            bfsq.put((ni, nj, grid[ni][nj]))
            todo.append((ni, nj, grid[ni][nj]))
            grid[ni][nj] = '@'
            nj += 1 if todo[-1][-1] == '[' else -1
            bfsq.put((ni, nj, grid[ni][nj]))
            todo.append((ni, nj, grid[ni][nj]))
            grid[ni][nj] = '@'
    else:
        for i, j, c in todo:
            grid[i][j] = '.'
        for i, j, c in todo:
            grid[i + di][j + dj] = c
        return (pos[0] + di, pos[1] + dj)
    for i, j, c in todo:
        grid[i][j] = c
    return pos


grid = []
with open('15.in') as file:
    for line in file:
        line = line.strip()
        if not line:
            m, n = len(grid), len(grid[0])
            pos = getstart(grid, m, n)
            continue
        elif line[0] == '#':
            grid.append([conv for c in line for conv in double[c]])
        else:
            for c in line:
                pos = move(grid, *dr[c], pos)

print(sum(
    100 * i + j for i, row in enumerate(grid) for j, c in enumerate(row)
    if c == '['
))
