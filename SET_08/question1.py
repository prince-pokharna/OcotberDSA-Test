x = int(input())

lo = 0
hi = 1000000001
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if mid * mid <= x:
        answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)