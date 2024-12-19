words, targets = [], []
with open('19.in') as file:
    for line in file:
        if not words:
            words = line.strip().split(', ')
        elif line.strip():
            targets.append(line.strip())
words.sort(key=len)


def count(target):
    n = len(target)
    cnt = [1] + [0] * n
    for i in range(n):
        if not cnt[i]:
            continue
        for word in words:
            if i + len(word) <= n:
                if target[i:i + len(word)] == word:
                    cnt[i + len(word)] += cnt[i]
            else:
                break
    return cnt[n]


print(sum(count(target) for target in targets))
