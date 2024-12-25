A = 50230824
prog = [2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0]


def work_simplified(A):
    while A:
        print(((A & 7) ^ 7 ^ (A // (1 << ((A & 7) ^ 3)))) & 7, end=",")
        A >>= 3


work_simplified(A)
