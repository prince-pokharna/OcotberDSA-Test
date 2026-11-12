def groups_needed(pages, limit):
    groups = 1
    current = 0
    for p in pages:
        if current + p > limit:
            groups += 1
            current = p
        else:
            current += p
    return groups


n, m = map(int, input().split())
pages = list(map(int, input().split()))

if m > n:
    print(-1)
else:
    biggest_book = 0
    total_pages = 0
    for p in pages:
        if p > biggest_book:
            biggest_book = p
        total_pages += p

    low = biggest_book
    high = total_pages

    while low < high:
        mid = (low + high) // 2
        if groups_needed(pages, mid) <= m:
            high = mid
        else:
            low = mid + 1

    print(low)