from itertools import pairwise
from functools import cache
from sortedcontainers import SortedList

pads = [["789", "456", "123", "#0A"], ["#^A", "<v>"]]
maps = [
    {c: (i, j) for i, row in enumerate(pad) for j, c in enumerate(row)}
    for pad in pads
]
moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1), 'A': (0, 0)}
A = maps[1]['A']


def move(pad, p, q):
    i, j = p[0] + moves[q][0], p[1] + moves[q][1]
    if 0 <= i < len(pad) and 0 <= j < len(pad[0]) and pad[i][j] != '#':
        return i, j
    return None


@cache
def mindist(start, end, pad, n):
    # Cost to go from:
    #   Start: start on pad (0: key, 1: arrow) and A on next arrow pad
    #   End: (end, A) and press A
    # Reachability problem: Dijkstra's algorithm
    #   Suppose we are at position (p1, p2) on the two pads
    #   Moving to (p1, q2) and pressing it costs f(q1, q2, 1, n - 1)
    #   Ensure that the keypress is valid and move
    if n == 1 or start == end:
        return abs(start[0] - end[0]) + abs(start[1] - end[1]) + 1
    dist, djset = {(start, A): 0}, SortedList([(0, (start, A))])
    while djset:
        d, (p1, q1) = djset.pop(0)
        if (p1, q1) == (end, A):
            return d
        for k, q2 in maps[1].items():
            if k in 'v^<>':
                if (p2 := move(pads[pad], p1, k)) is None:
                    continue
            elif k == '#' or p1 != (p2 := end):
                continue
            cost, newstate = mindist(q1, q2, 1, n - 1), (p2, q2)
            if newstate in dist and dist[newstate] > d + cost:
                djset.remove((dist[newstate], newstate))
                dist.pop(newstate)
            if newstate not in dist:
                dist[newstate] = d + cost
                djset.add((d + cost, newstate))


def minsteps(code, n):
    return sum(
        mindist(maps[0][x], maps[0][y], 0, n) for x, y in pairwise('A' + code)
    )


with open('21.in') as file:
    print(sum(minsteps(s := line.strip(), 3) * int(s[:-1]) for line in file))
with open('21.in') as file:
    print(sum(minsteps(s := line.strip(), 26) * int(s[:-1]) for line in file))
