n = int(input())
ids = list(map(int, input().split()))

candidate = 0
count = 0
for x in ids:
    if count == 0:
        candidate = x
    if x == candidate:
        count += 1
    else:
        count -= 1

print(candidate)