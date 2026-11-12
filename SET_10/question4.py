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


n = int(input())
a = list(map(int, input().split()))

a = merge_sort(a)
found = False

for i in range(n - 2):
    if a[i] > 0:
        break
    if i > 0 and a[i] == a[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:
        total = a[i] + a[left] + a[right]
        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            print(a[i], a[left], a[right])
            found = True
            left += 1
            right -= 1
            while left < right and a[left] == a[left - 1]:
                left += 1
            while left < right and a[right] == a[right + 1]:
                right -= 1

if not found:
    print("None")