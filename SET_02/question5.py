def reverse_part(a, left, right):
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1


n, k = map(int, input().split())
a = list(map(int, input().split()))

k = k % n

reverse_part(a, 0, n - 1)
reverse_part(a, 0, k - 1)
reverse_part(a, k, n - 1)

print(" ".join(map(str, a)))