s = input().strip()
p = input().strip()

n = len(s)
m = len(p)
result = []

if m <= n:
    need = [0] * 26
    have = [0] * 26

    for i in range(m):
        need[ord(p[i]) - 97] += 1
        have[ord(s[i]) - 97] += 1

    if need == have:
        result.append(0)

    for i in range(m, n):
        have[ord(s[i]) - 97] += 1
        have[ord(s[i - m]) - 97] -= 1
        if need == have:
            result.append(i - m + 1)

if len(result) == 0:
    print("None")
else:
    print(" ".join(map(str, result)))