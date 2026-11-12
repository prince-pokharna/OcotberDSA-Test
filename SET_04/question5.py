n = int(input())
a = list(map(int, input().split()))

last = {}
left = 0
best = 0

for right in range(n):
    x = a[right]
    if x in last and last[x] >= left:
        left = last[x] + 1
    last[x] = right
    length = right - left + 1
    if length > best:
        best = length

print(best)