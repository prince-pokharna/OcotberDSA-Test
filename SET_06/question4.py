def comes_first(x, y):
    if freq[x] != freq[y]:
        return freq[x] < freq[y]
    return x > y


def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if comes_first(left[i], right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


n = int(input())
ids = list(map(int, input().split()))

freq = {}
for x in ids:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

unique_ids = []
for x in freq:
    unique_ids.append(x)

unique_ids = merge_sort(unique_ids)

result = []
for x in unique_ids:
    for _ in range(freq[x]):
        result.append(str(x))

print(" ".join(result))