n, k, t = map(int, input().split())
a = list(map(int, input().split()))

need = k * t

window = 0
for i in range(k):
    window += a[i]

count = 0
if window >= need:
    count += 1

for i in range(k, n):
    window += a[i] - a[i - k]
    if window >= need:
        count += 1

print(count)