def merge_sort(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2
    left, left_count = merge_sort(a[:mid])
    right, right_count = merge_sort(a[mid:])

    merged = []
    count = left_count + right_count
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, count


n = int(input())
scores = list(map(int, input().split()))

sorted_scores, inversions = merge_sort(scores)
print(inversions)