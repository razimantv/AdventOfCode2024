from collections import defaultdict
from itertools import combinations
adj: defaultdict[int, set[int]] = defaultdict(set)


def fix(seq: list[int]) -> list[int]:
    for u, v in combinations(seq, 2):
        if v not in adj[u]:
            break
    else:
        return seq
    fixed: list[int] = []
    for u in seq:
        for i, v in enumerate(fixed):
            if v in adj[u]:
                fixed.insert(i, u)
                break
        else:
            fixed.append(u)
    return fixed


ret = [0, 0]
with open('5.in') as file:
    for line in file:
        if line[0] == '\n':
            break
        u, v = map(int, line[:-1].split('|'))
        adj[u].add(v)

    for line in file:
        seq = list(map(int, line[:-1].split(',')))
        fixed = fix(seq)
        ret[fixed == seq] += fixed[len(fixed) // 2]

print(ret)
