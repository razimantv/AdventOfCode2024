A = 50230824
prog = [2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0]


def combo(op, a, b, c):
    if op < 4:
        return op
    else:
        return [a, b, c][op - 4]


def operate(i, a, b, c):
    op = prog[i]
    x = prog[i + 1]
    if op == 0:
        a //= (1 << combo(x, a, b, c))
    elif op == 1:
        b ^= x
    elif op == 2:
        b = combo(x, a, b, c) & 7
    elif op == 3:
        if a:
            i = x - 2
    elif op == 4:
        b ^= c
    elif op == 5:
        print(f"{combo(x, a, b, c) & 7},", end="")
    elif op == 6:
        b = a // (1 << combo(x, a, b, c))
    elif op == 7:
        c = a // (1 << combo(x, a, b, c))
    return i + 2, a, b, c


def work(A):
    i, B, C = 0, 0, 0
    while i < len(prog):
        i, A, B, C = operate(i, A, B, C)


def work_simplified(A):
    while A:
        print(((A & 7) ^ 7 ^ (A // (1 << ((A & 7) ^ 3)))) & 7, end=",")
        A >>= 3


work(A)
print('')
work_simplified(A)
