from functools import cache

with open('11.in') as file:
    input = [map(int, line.strip().split()) for line in file][0]


@cache
def count_after(n, d):
    if d == 0:
        return 1
    elif n == 0:
        return count_after(1, d - 1)
    elif (l := len(s := str(n))) % 2 == 0:
        return (
            count_after(int(s[:l // 2]), d - 1) +
            count_after(int(s[l // 2:]), d - 1)
        )
    else:
        return count_after(2024 * n, d - 1)


print(sum(count_after(n, 25) for n in input))
print(sum(count_after(n, 75) for n in input))
