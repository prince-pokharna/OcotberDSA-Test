n = int(input())
a = list(map(int, input().split()))
x = int(input())

lo = 0
hi = n
while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid] < x:
        lo = mid + 1
    else:
        hi = mid
first = lo

lo = 0
hi = n
while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid] <= x:
        lo = mid + 1
    else:
        hi = mid
last = lo - 1

if first < n and a[first] == x:
    print(first, last)
else:
    print(-1, -1)