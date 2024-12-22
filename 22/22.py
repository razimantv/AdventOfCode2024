from collections import defaultdict

mod = 0xffffff
tot = defaultdict(int)

def next(x, n):
    diff, seen = 0, set()
    for i in range(n):
        last = x
        x = (x ^ (x << 6)) & mod
        x = (x ^ (x >> 5)) & mod
        x = (x ^ (x << 11)) & mod
        diff = ((diff << 5) | ((d := x % 10) - last % 10 + 9)) & 0xfffff
        if i > 2 and diff not in seen:
                seen.add(diff)
                tot[diff] += d
    return x


with open('22.in') as file:
    print(sum(next(int(line.strip()), 2000) for line in file))
print(max(tot.values()))
