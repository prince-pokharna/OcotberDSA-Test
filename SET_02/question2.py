n = int(input())
ids = list(map(int, input().split()))

count = {}
for x in ids:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

answer = -1
for x in ids:
    if count[x] == 1:
        answer = x
        break

print(answer)