from collections import defaultdict, Counter
from itertools import combinations

with open('8.in') as file:
    grid = [line.strip() for line in file]

pos = defaultdict(list)
m, n = len(grid), len(grid[0])
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell != '.':
            pos[cell].append((i, j))

def check(i, j):
    for group in pos.values():
        for (i1, j1), (i2, j2) in combinations(group, 2):
            if (i - i1) * (j - j2) == (j - j1) * (i - i2):
                return True
    return False

print(sum(check(i, j) for i in range(m) for j in range(n)))
