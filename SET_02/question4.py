import sys

data = sys.stdin.read().split()
n = int(data[0])
q = int(data[1])

sales = []
for i in range(n):
    sales.append(int(data[2 + i]))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + sales[i]

pos = 2 + n
answers = []
for _ in range(q):
    l = int(data[pos])
    r = int(data[pos + 1])
    pos += 2
    answers.append(str(prefix[r + 1] - prefix[l]))

print("\n".join(answers))