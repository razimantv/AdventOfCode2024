import re
import math

regex = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
X, Y = 101, 103
grid = [[0] * X for _ in range(Y)]


def work(N):
    edges = 0
    for x, y, vx, vy in points:
        x = ((x + N * vx) % X + X) % X
        y = ((y + N * vy) % Y + Y) % Y
        grid[y][x] = N
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < X and 0 <= ny < Y and grid[ny][nx] == N:
                edges += 1
    return edges


with open('14.in') as file:
    points = [
        list(map(int, re.match(regex, line).groups())) for line in file
    ]
print(max(range(1, X * Y), key=work))
