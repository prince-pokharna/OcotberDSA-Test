n = int(input())
marks = list(map(int, input().split()))

counts = [0] * 101
for m in marks:
    counts[m] += 1

result = []
for value in range(101):
    for _ in range(counts[value]):
        result.append(str(value))

print(" ".join(result))