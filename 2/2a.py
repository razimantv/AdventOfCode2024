import numpy as np
from itertools import pairwise
from collections import Counter

ret = 0
good = [[-3, -1], [1, 3]]
with open('2.in') as file:
    for line in file:
        report = map(int, line.split())
        diffs = Counter(y-x for x, y in pairwise(report))
        a, b = min(diffs), max(diffs)
        if -3 <= a <= b <= -1 or 1 <= a <= b <= 3:
            ret += 1
print(ret)
