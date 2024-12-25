ops = [
    lambda x, y: x + y, lambda x, y: x * y,
    lambda x, y: int(str(x) + str(y))
]
def good(target, nums, ops):
    poss = set([nums[0]])
    for x in nums[1:]:
        new_poss = set()
        for p in poss:
            for y in [op(p, x) for op in ops]:
                if y <= target:
                    new_poss.add(y)
        poss = new_poss
    return target in poss


ret = [0, 0]
with open('7.in') as file:
    for line in file:
        lhs, rhs = line[:-1].split(': ')
        lhs = int(lhs)
        rhs = list(map(int, rhs.split(' ')))
        if good(lhs, rhs, ops[:2]):
            ret[0] += lhs
        if good(lhs, rhs, ops):
            ret[1] += lhs
print(ret)
