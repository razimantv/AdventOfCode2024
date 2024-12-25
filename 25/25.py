from functools import reduce
from operator import or_
from itertools import batched, combinations


def mask(grid):
    return reduce(or_, (1 << i for i, c in enumerate(grid) if c == '#'), 0)


with open('25.in') as file:
    masks = [
        mask(''.join(line.strip() for line in grid))
        for grid in batched(file, 8)
    ]
print(sum(1 for x, y in combinations(masks, 2) if x & y == 0))
