OFFSET = 1000
MAX = 2000

array = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    for j in range(x1, x2):
        for k in range(y1, y2):
            array[j][k] = i + 1

min_x, max_x, min_y, max_y = MAX, 0, MAX, 0
exist = False

for i in range(MAX + 1):
    for j in range(MAX + 1):
        if array[i][j] == 1:
            exist = True
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

if exist:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
else:
    area = 0

print(area)