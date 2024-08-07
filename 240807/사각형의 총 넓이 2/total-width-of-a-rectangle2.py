OFFSET = 100
# 2차원 평면
array = [[0] * (OFFSET * 2 + 1) for _ in range(OFFSET * 2 + 1)]
# 사각형 개수
n = int(input())
# 사각형 입력
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 + OFFSET, x2 + OFFSET):
        for j in range(y1 + OFFSET, y2 + OFFSET):
            array[i][j] = 1

# 넓이 count
count = 0
for items in array:
    for item in items:
        if item == 1:
            count += 1

print(count)