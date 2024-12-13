import re
import math

with open('13.in') as file:
    input = list(map(int, re.findall(r'\d+', file.read())))
n = len(input)


def work(ar):
    a, c, b, d, e, f = ar
    e, f = e + 10 ** 13, f + 10 ** 13
    det = a * d - b * c
    t1 = d * e - b * f
    t2 = -c * e + a * f
    if t1 % det == 0 and t2 % det == 0:
        m1, m2 = t1 // det, t2 // det
        if m1 >= 0 and m2 >= 0:
            return 3 * m1 + m2
    return 0


print(sum(work(input[i:i + 6]) for i in range(0, n, 6)))
