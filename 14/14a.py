import re
import math

regex = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
X, Y, N = 101, 103, 100
cnt = [0] * 4


def work(x, y, vx, vy):
    x = ((x + N * vx) % X + X) % X
    y = ((y + N * vy) % Y + Y) % Y
    if x != X // 2 and y != Y // 2:
        cnt[(x < X // 2) + 2 * (y < Y // 2)] += 1


with open('14.in') as file:
    for line in file:
        x, y, vx, vy = map(int, re.match(regex, line).groups())
        work(x, y, vx, vy)

print(math.prod(cnt))
