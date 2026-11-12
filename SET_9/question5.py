n = int(input())
calendar = []
for _ in range(n):
    start, end = map(int, input().split())
    calendar.append([start, end])

new_start, new_end = map(int, input().split())

i = 0

while i < n and calendar[i][1] < new_start:
    print(calendar[i][0], calendar[i][1])
    i += 1

while i < n and calendar[i][0] <= new_end:
    if calendar[i][0] < new_start:
        new_start = calendar[i][0]
    if calendar[i][1] > new_end:
        new_end = calendar[i][1]
    i += 1

print(new_start, new_end)

while i < n:
    print(calendar[i][0], calendar[i][1])
    i += 1