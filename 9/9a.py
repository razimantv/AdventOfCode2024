with open('9.in') as file:
    line = [line.strip() for line in file][0]

disk = []
for i, c in enumerate(line):
    x = int(c)
    disk += [-1] * x if i & 1 else [i // 2] * x

l, r = 0, len(disk) - 1
while l < r:
    if disk[r] == -1:
        r -= 1
    elif disk[l] == -1:
        disk[l] = disk[r]
        disk[r] = -1
        l += 1
        r -= 1
    else:
        l += 1

print(sum(i * x for i, x in enumerate(disk) if x != -1))
