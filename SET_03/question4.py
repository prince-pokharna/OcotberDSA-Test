import sys

data = sys.stdin.read().split()
m = int(data[0])
n = int(data[1])

A = []
for i in range(m + n):
    A.append(int(data[2 + i]))

B = []
for i in range(n):
    B.append(int(data[2 + m + n + i]))

i = m - 1
j = n - 1
k = m + n - 1

while j >= 0:
    if i >= 0 and A[i] > B[j]:
        A[k] = A[i]
        i -= 1
    else:
        A[k] = B[j]
        j -= 1
    k -= 1

print(" ".join(map(str, A)))