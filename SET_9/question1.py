n = int(input())
prices = list(map(int, input().split()))
target = int(input())

left = 0
right = n - 1

while left < right:
    total = prices[left] + prices[right]
    if total == target:
        print(left + 1, right + 1)
        break
    elif total < target:
        left += 1
    else:
        right -= 1