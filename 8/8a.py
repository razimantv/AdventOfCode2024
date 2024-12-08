from collections import defaultdict
from itertools import combinations

with open('8.in') as file:
    grid = [line.strip() for line in file]

pos = defaultdict(list)
m, n = len(grid), len(grid[0])
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell != '.':
            pos[cell].append((i, j))

antinodes = set()
for group in pos.values():
    for (i1, j1), (i2, j2) in combinations(group, 2):
        i, j = 2 * i2 - i1, 2 * j2 - j1
        if 0 <= i < m and 0 <= j < n:
            antinodes.add((i, j))
        i, j = 2 * i1 - i2, 2 * j1 - j2
        if 0 <= i < m and 0 <= j < n:
            antinodes.add((i, j))

print(len(antinodes))
