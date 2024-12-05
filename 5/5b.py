from collections import defaultdict
from itertools import combinations

adj: defaultdict[int, set[int]] = defaultdict(set)

ret = 0
with open('5.in') as file:
    for line in file:
        if line[0] == '\n':
            break
        u, v = map(int, line[:-1].split('|'))
        adj[u].add(v)

    for line in file:
        seq = list(map(int, line[:-1].split(',')))
        for u, v in combinations(seq, 2):
            if v in adj[u]:
                continue
            newseq: list[int] = []
            for u in seq:
                for i, v in enumerate(newseq):
                    if v in adj[u]:
                        newseq.insert(i, u)
                        break
                else:
                    newseq.append(u)
            ret += newseq[len(newseq) // 2]
            print(seq, newseq)
            break

print(ret)
