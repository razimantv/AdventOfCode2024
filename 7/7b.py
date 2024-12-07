def good(target, nums):
    poss = set([nums[0]])
    for x in nums[1:]:
        new_poss = set()
        for p in poss:
            for y in [p + x, p * x, int(str(p) + str(x))]:
                if y <= target:
                    new_poss.add(y)
        poss = new_poss
    return target in poss

ret = 0
with open('7.in') as file:
    for line in file:
        lhs, rhs = line[:-1].split(': ')
        lhs = int(lhs)
        rhs = list(map(int, rhs.split(' ')))
        if good(lhs, rhs):
            ret += lhs
print(ret)
