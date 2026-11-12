import sys

data = sys.stdin.read().split()
m = int(data[0])
n = int(data[1])

A = []
for i in range(m):
    A.append(int(data[2 + i]))

B = []
for i in range(n):
    B.append(int(data[2 + m + i]))

i = 0
j = 0
result = []

while i < m and j < n:
    if A[i] < B[j]:
        result.append(A[i])
        i += 1
    elif A[i] > B[j]:
        result.append(B[j])
        j += 1
    else:
        result.append(A[i])
        i += 1
        j += 1

while i < m:
    result.append(A[i])
    i += 1

while j < n:
    result.append(B[j])
    j += 1

print(" ".join(map(str, result)))