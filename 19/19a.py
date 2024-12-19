words, targets = [], []
with open('19.in') as file:
    for line in file:
        if not words:
            words = line.strip().split(', ')
        elif line.strip():
            targets.append(line.strip())
words.sort(key=len)


def poss(target):
    n = len(target)
    poss = [True] + [False] * n
    for i in range(n):
        if not poss[i]:
            continue
        for word in words:
            if i + len(word) <= n:
                if target[i:i + len(word)] == word:
                    poss[i + len(word)] = True
            else:
                break
    return poss[n]


print(sum(poss(target) for target in targets))
