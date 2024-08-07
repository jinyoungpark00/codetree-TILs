OFFSET = 100
MAX = 200

array = [[0] * (MAX + 1) for _ in range(MAX + 1)]

n = int(input())

is_blue = True
for i in range(n):
    is_blue = not is_blue # 색 변경
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    # 파란색 = 1
    if is_blue:
        for x in range(x1, x2):
            for y in range(y1, y2):
                array[x][y] = 1
    # 빨간색 = 2
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                array[x][y] = 2

# 파란색 개수 check
count = 0
for row in array:
    for item in row:
        if item == 1:
            count += 1

print(count)