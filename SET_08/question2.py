import sys

data = sys.stdin.read().split()
R = int(data[0])
C = int(data[1])

grid = []
pos = 2
for i in range(R):
    row = []
    for j in range(C):
        row.append(int(data[pos]))
        pos += 1
    grid.append(row)

t = int(data[pos])

lo = 0
hi = R * C - 1
found_row = -1
found_col = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2
    value = grid[mid // C][mid % C]
    if value == t:
        found_row = mid // C
        found_col = mid % C
        break
    elif value < t:
        lo = mid + 1
    else:
        hi = mid - 1

print(found_row, found_col)