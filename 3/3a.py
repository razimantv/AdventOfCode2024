import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
ret = 0
with open('3.in') as file:
    for line in file:
        matches = re.findall(pattern, line)
        ret += sum([int(x) * int(y) for x, y in matches])

print(ret)
