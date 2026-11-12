n, k = map(int, input().split())
ids = list(map(int, input().split()))

last = {}
alert = False

for i in range(n):
    x = ids[i]
    if x in last and i - last[x] <= k:
        alert = True
        break
    last[x] = i

if alert:
    print("YES")
else:
    print("NO")