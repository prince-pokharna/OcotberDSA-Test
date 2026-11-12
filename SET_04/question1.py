n, k = map(int, input().split())
a = list(map(int, input().split()))

window = 0
for i in range(k):
    window += a[i]

best = window
for i in range(k, n):
    window += a[i] - a[i - k]
    if window > best:
        best = window

print(best)