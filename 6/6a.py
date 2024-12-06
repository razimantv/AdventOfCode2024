neigh = [[-1, 0], [0, 1], [1, 0], [0, -1]]

with open('6.in') as file:
    grid = [list(line[:-1]) for line in file]
m, n = len(grid), len(grid[0])

for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == '^':
            break
    else:
        continue
    break

dir = 0
while 0 <= i < m and 0 <= j < n:
    ii, jj = i + neigh[dir][0], j + neigh[dir][1]
    grid[i][j] = 's'
    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '#':
        dir = (dir + 1) & 3
    else:
        i, j = ii, jj

print(sum(line.count('s') for line in grid))
