n, D = map(int, input().split())
weights = list(map(int, input().split()))

heaviest = 0
total = 0
for w in weights:
    if w > heaviest:
        heaviest = w
    total += w

lo = heaviest
hi = total

while lo < hi:
    mid = (lo + hi) // 2
    days = 1
    load = 0
    for w in weights:
        if load + w > mid:
            days += 1
            load = w
        else:
            load += w
    if days <= D:
        hi = mid
    else:
        lo = mid + 1

print(lo)