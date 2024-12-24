value, rules = {}, {}
with open('24.in') as file:
    for line in file:
        parts = line.strip().split(' ')
        if len(parts) == 2:
            value[parts[0][:-1]] = int(parts[1])
        elif len(parts) == 5:
            rules[parts[4]] = [
                parts[1], min(parts[0], parts[2]), max(parts[0], parts[2])
            ]


def adder(n):
    s, c, dprev, C, d = None, None, None, None, None
    for k, v in rules.items():
        if v[1] == f'x{n:02}':
            if v[0] == 'XOR':
                s = k
            elif v[0] == 'AND':
                c = k
    op, x1, x2 = rules[f'z{n:02}']
    if op == 'XOR':
        if x1 == s:
            dprev = x2
        elif x2 == s:
            dprev = x1
        else:
            print(f'z{n:02}', rules[f'z{n:02}'])
    for k, v in rules.items():
        if v[1:] == [s, dprev] or v[1:] == [dprev, s]:
            if v[0] == 'AND':
                C = k
        elif s in v[1:] or dprev in v[1:]:
            print(k, v)
    for k, v in rules.items():
        if v[1:] == [C, c] or v[1:] == [c, C]:
            if v[0] == 'OR':
                d = k
            else:
                print(k, v)

    return s, c, dprev, C, d


printed = False
for i in range(45):
    cur = adder(i)
    if i > 1 and cur[2] != prev[-1]:
        if not printed:
            print(i, prev, cur, '\n')
            printed = True
    else:
        printed = False
    prev = cur
