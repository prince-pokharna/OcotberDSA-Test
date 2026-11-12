n = int(input())
ids = list(map(int, input().split()))

seen = set()
answer = -1
for x in ids:
    if x in seen:
        answer = x
        break
    seen.add(x)

print(answer)