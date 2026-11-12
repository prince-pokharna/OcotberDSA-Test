n = int(input())
a = list(map(int, input().split()))
t = int(input())

lo = 0
hi = n

while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid] < t:
        lo = mid + 1
    else:
        hi = mid

print(lo)