A = 50230824
prog = [2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0]


def next(A):
    return ((A & 7) ^ 7 ^ (A // (1 << ((A & 7) ^ 3)))) & 7

while A:
    print(next(A), end=",")
    A >>= 3
print()

poss = [0]
for x in prog[::-1]:
    nextposs = []
    for y in poss:
        for z in range(y << 3, (y << 3) + 8):
            if next(z) == x:
                nextposs.append(z)
    poss = nextposs

print(poss[0])
