OFFSET = 100
MAX = OFFSET * 2

array = [[0] * (MAX + 1) for _ in range(MAX + 1)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x += OFFSET
    y += OFFSET

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            array[i][j] = 1

count = 0
for row in array:
    for item in row:
        if item == 1:
            count += 1

print(count)