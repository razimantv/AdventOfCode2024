import numpy as np
from collections import Counter

with open('1.in') as file:
    grid = np.array([[int(x) for x in line.split()] for line in file])

ctrs = [Counter(row) for row in grid.T]
print(sum(k * v * ctrs[1][k] for k, v in ctrs[0].items()))
