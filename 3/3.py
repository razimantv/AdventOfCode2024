import re

mul = r"mul\((\d{1,3}),(\d{1,3})\)"
do, dont = r"do\(\)", r"don't\(\)"

with open('3.in') as file:
    input = ''.join(line.strip() for line in file)

do_matches, dont_matches = [
    [match.start() for match in re.finditer(pattern, input)] + [len(input)]
    for pattern in [do, dont]
]
ret, good, i, j = [0, 0], True, 0, 0
for match in re.finditer(mul, input):
    while match.start() > min(do_matches[i], dont_matches[j]):
        if do_matches[i] < dont_matches[j]:
            i, good = i + 1, True
        else:
            j, good = j + 1, False
    ret[0] += (cur := int(match.group(1)) * int(match.group(2)))
    if good:
        ret[1] += cur

print(ret)
