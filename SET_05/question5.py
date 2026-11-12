import random

n, k = map(int, input().split())
a = list(map(int, input().split()))

target = n - k
lo = 0
hi = n - 1

while True:
    pivot = a[random.randint(lo, hi)]
    lt = lo
    i = lo
    gt = hi

    while i <= gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    if target < lt:
        hi = lt - 1
    elif target > gt:
        lo = gt + 1
    else:
        print(pivot)
        break