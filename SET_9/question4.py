def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(items):
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    return merge(left, right)


n = int(input())
bookings = []
for _ in range(n):
    start, end = map(int, input().split())
    bookings.append([start, end])

bookings = merge_sort(bookings)

current_start = bookings[0][0]
current_end = bookings[0][1]

for i in range(1, n):
    start = bookings[i][0]
    end = bookings[i][1]
    if start <= current_end:
        if end > current_end:
            current_end = end
    else:
        print(current_start, current_end)
        current_start = start
        current_end = end

print(current_start, current_end)