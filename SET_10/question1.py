n = int(input())
a = list(map(int, input().split()))

result = [0] * n
left = 0
right = n - 1
position = n - 1

while left <= right:
    left_square = a[left] * a[left]
    right_square = a[right] * a[right]
    if left_square > right_square:
        result[position] = left_square
        left += 1
    else:
        result[position] = right_square
        right -= 1
    position -= 1

print(" ".join(map(str, result)))