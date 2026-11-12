n = int(input())
a = list(map(int, input().split()))

lo = 0
hi = n - 1

while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid] > a[hi]:
        lo = mid + 1
    else:
        hi = mid

print(a[lo])