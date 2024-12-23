from collections import defaultdict
from itertools import combinations

graph = defaultdict(set)
with open('23.in') as file:
    for line in file:
        u, v = line.strip().split('-')
        graph[u].add(v)
        graph[v].add(u)


def largest_clique(cur, largest):
    if len(cur) > len(largest[0]):
        largest[0] = cur
    for v in graph[u := cur[-1]]:
        if v > u and all(w in graph[v] for w in cur[:-1]):
            largest_clique(cur + [v], largest)


largest = [[]]
for u in graph:
    largest_clique([u], largest)
print(','.join(largest[0]))
