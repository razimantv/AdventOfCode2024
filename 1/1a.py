import numpy as np

with open('1a.in') as file:
    grid = np.array([[int(x) for x in line.split()] for line in file])

print(sum(abs(x - y) for x, y in zip(sorted(grid[:, 0]), sorted(grid[:, 1]))))
