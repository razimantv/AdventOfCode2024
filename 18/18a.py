L = 71
dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
with open('18.in') as file:
    bad = [tuple(map(int, line.strip().split(','))) for line in file]


def dist(n):
    grid = [[-1] * L for _ in range(L)]
    for i, j in bad[:n]:
        grid[i][j] = -2

    grid[0][0] = 0
    todo = [(0, 0)]
    while todo:
        next = []
        for i, j in todo:
            for di, dj in dr:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < L and grid[ni][nj] == -1:
                    grid[ni][nj] = grid[i][j] + 1
                    next.append((ni, nj))
        todo = next
    return grid[-1][-1]


print(dist(1024))
