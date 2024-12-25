from functools import cache, reduce
from operator import or_, and_, xor

ops = {'AND': and_, 'OR': or_, 'XOR': xor}
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


@cache
def calculate(x):
    if x in value:
        return value[x]
    op, x1, x2 = rules[x]
    return ops[op](calculate(x1), calculate(x2))


print(reduce(or_, (calculate(z) << int(z[1:]) for z in rules if z[0] == 'z')))
