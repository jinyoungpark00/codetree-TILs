OFFSET = 1000
# 2차원 좌표평면
array = [[0] * (OFFSET * 2 + 1) for _ in range(OFFSET * 2 + 1)]

# 직사각형 입력
for i in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    # 사각형 a, b
    if i < 2:
        for j in range(x1 + OFFSET, x2 + OFFSET):
            for k in range(y1 + OFFSET, y2 + OFFSET):
                array[j][k] = 1
    # 사각형 m
    else:
        for j in range(x1 + OFFSET, x2 + OFFSET):
            for k in range(y1 + OFFSET, y2 + OFFSET):
                array[j][k] = 0


# 넓이 계산
count = 0
for items in array:
    for item in items:
        if item == 1:
            count += 1

print(count)