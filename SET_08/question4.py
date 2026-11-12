n = int(input())
a = list(map(int, input().split()))
t = int(input())

lo = 0
hi = n - 1
answer = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == t:
        answer = mid
        break
    if a[lo] <= a[mid]:
        if a[lo] <= t and t < a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    else:
        if a[mid] < t and t <= a[hi]:
            lo = mid + 1
        else:
            hi = mid - 1

print(answer)