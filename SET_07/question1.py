n = int(input())
a = list(map(int, input().split()))
q = int(input())

lo = 0
hi = n - 1
answer = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == q:
        answer = mid
        break
    elif a[mid] < q:
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)