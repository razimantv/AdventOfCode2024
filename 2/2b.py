import numpy as np
from itertools import pairwise
from collections import Counter

good = [[-3, -1], [1, 3]]


def isgood(report):
    diffs = Counter(y-x for x, y in pairwise(report))
    a, b = min(diffs), max(diffs)
    return (-3 <= a <= b <= -1 or 1 <= a <= b <= 3)


ret = 0
with open('2.in') as file:
    for line in file:
        report = list(map(int, line.split()))
        for i in range(len(report) + 1):
            if isgood(report[:i] + report[i+1:]):
                ret += 1
                break
print(ret)
