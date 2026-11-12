n = int(input())
a = list(map(int, input().split()))
h = int(input())

lo = 0
hi = n - 1
while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid] < a[mid + 1]:
        lo = mid + 1
    else:
        hi = mid
peak = lo

answer = -1

left = 0
right = peak
while left <= right:
    mid = left + (right - left) // 2
    if a[mid] == h:
        answer = mid
        break
    elif a[mid] < h:
        left = mid + 1
    else:
        right = mid - 1

if answer == -1:
    left = peak + 1
    right = n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == h:
            answer = mid
            break
        elif a[mid] > h:
            left = mid + 1
        else:
            right = mid - 1

print(answer)