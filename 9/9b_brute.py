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

ret = 0
for start, id, size in files[::-1]:
    i = 0
    while i < len(spaces):
        sstart, ssize = spaces[i]
        if sstart >= start:
            spaces.pop(i)
            continue
        elif ssize >= size:
            start = sstart
            if ssize == size:
                spaces.pop(i)
            else:
                spaces[i] = sstart + size, ssize - size
            break
        i += 1
    ret += (2 * start + size - 1) * size * id // 2

print(ret)
