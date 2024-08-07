MAX = 200000
OFFSET = 100000
# 타일 list [1 = black, 2 = white]
tile = [0] * (MAX + 1)
# 시작 인덱스
start = OFFSET

# 명령어 수 입력
n = int(input())
# 명령 입력
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)
    # 타일 뒤집기
    # 오른쪽
    if direction == 'R':
        for i in range(start, start + distance):
            tile[i] = 1
        start += (distance - 1)
    # 왼쪽
    else:
        for i in range(start, start - distance, -1):
            tile[i] = 2
        start -= (distance - 1)

black = 0
white = 0

# 타일 수 계산
for item in tile:
    if item == 1:
        black += 1
    elif item == 2:
        white += 1

print(white, black)