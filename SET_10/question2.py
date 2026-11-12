n = int(input())
prices = list(map(int, input().split()))
q = int(input())

floor_value = None
ceiling_value = None

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2
    if prices[mid] == q:
        floor_value = q
        ceiling_value = q
        break
    elif prices[mid] < q:
        floor_value = prices[mid]
        low = mid + 1
    else:
        ceiling_value = prices[mid]
        high = mid - 1

if floor_value is None:
    floor_value = "None"
if ceiling_value is None:
    ceiling_value = "None"

print(floor_value, ceiling_value)