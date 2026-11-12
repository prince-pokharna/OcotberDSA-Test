def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    return merge(left, right)


m, n = map(int, input().split())
sheet_a = list(map(int, input().split()))
sheet_b = list(map(int, input().split()))

ids_in_a = set(sheet_a)
already_added = set()
common = []

for x in sheet_b:
    if x in ids_in_a and x not in already_added:
        already_added.add(x)
        common.append(x)

common = merge_sort(common)

if len(common) == 0:
    print("None")
else:
    print(" ".join(map(str, common)))