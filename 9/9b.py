with open('9.in') as file:
    line = [line.strip() for line in file][0]

files, spaces = [], []
pos = 0
for i, c in enumerate(line):
    x = int(c)
    if i % 2:
        spaces.append((pos, x))
    else:
        files.append((pos, i // 2, x))
    pos += x

n = len(spaces)
base = 1
while base < n:
    base <<= 1
seg = [(0, 0)] * (2 * base)
seg[base:base + n] = spaces
for i in range(base - 1, 0, -1):
    if seg[2 * i][1] < seg[2 * i + 1][1]:
        seg[i] = seg[2 * i + 1]
    else:
        seg[i] = seg[2 * i]

def query(value):
    if seg[1][1] < value:
        return -1
    node = 1
    while node < base:
        lc = node << 1
        if seg[lc][1] >= value:
            node = lc
        else:
            node = lc ^ 1
    return node

def update(node, sub):
    seg[node] = (seg[node][0] + sub, seg[node][1] - sub)
    while node > 1:
        node >>= 1
        if seg[2 * node][1]  < seg[2 * node + 1][1]:
            seg[node] = seg[2 * node + 1]
        else:
            seg[node] = seg[2 * node]

ret = 0
for start, id, size in files[::-1]:
    node = query(size)
    if node != -1 and seg[node][0] < start:
        start = seg[node][0]
        update(node, size)
    ret += (2 * start + size - 1) * size * id // 2

print(ret)
