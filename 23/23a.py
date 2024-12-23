from collections import defaultdict
from itertools import combinations

graph = defaultdict(set)
with open('23.in') as file:
    for line in file:
        u, v = line.strip().split('-')
        graph[u].add(v)
        graph[v].add(u)

triplets = set()
for u, vertices in graph.items():
    if u[0] != 't':
        continue
    for v, w in combinations(vertices, 2):
        if w in graph[v]:
            triplets.add(tuple(sorted([u, v, w])))
print(len(triplets))
