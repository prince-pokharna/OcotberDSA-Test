n = int(input())
a = list(map(int, input().split()))

pos = 0
for i in range(n):
    if a[i] != 0:
        a[pos], a[i] = a[i], a[pos]
        pos += 1

print(" ".join(map(str, a)))