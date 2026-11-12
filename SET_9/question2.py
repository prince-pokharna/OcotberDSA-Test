n, t = map(int, input().split())
scores = list(map(int, input().split()))

count = [0] * 101
for s in scores:
    count[s] += 1

sorted_scores = []
for value in range(101):
    for _ in range(count[value]):
        sorted_scores.append(value)

total = 0
for i in range(t, n - t):
    total += sorted_scores[i]

average = total / (n - 2 * t)
print("%.2f" % average)