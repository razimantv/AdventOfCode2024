import re

mul = r"mul\((\d{1,3}),(\d{1,3})\)"
do = r"do\(\)"
dont = r"don't\(\)"

with open('3.in') as file:
    input = ''.join(line for line in file)

ret, good = 0, True
do_matches = [match.start() for match in re.finditer(do, input)]
dont_matches = [match.start() for match in re.finditer(dont, input)]
i, j = 0, 0
for match in re.finditer(mul, input):
    while True:
        if i < len(do_matches) and do_matches[i] < match.start() and (
                j >= len(dont_matches) or do_matches[i] < dont_matches[j]
        ):
            i += 1
            good = True
        elif j < len(dont_matches) and dont_matches[j] < match.start() and (
            i >= len(do_matches) or dont_matches[j] < do_matches[i]
        ):
            j += 1
            good = False
        else:
            break
    if good:
        ret += int(match.group(1)) * int(match.group(2))

print(ret)
