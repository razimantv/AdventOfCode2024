def process(grid):
    keylock = 0 if grid[0][0] == '#' else 1
    return keylock, [
        sum(1 for i in range(1, 6) if grid[i][j] == '#')
        for j in range(5)
    ]


with open('25.in') as file:
    input = [line.strip() for line in file]

patterns, ret = [[], []], 0
for i in range(0, len(input), 8):
    keylock, pattern = process(input[i:i + 7])
    patterns[keylock].append(pattern)
    for other in patterns[1 - keylock]:
        if all(p + q <= 5 for p, q in zip(pattern, other)):
            ret += 1
print(ret)
