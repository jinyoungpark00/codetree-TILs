MAX = 200000
OFFSET = 100000
# black -> 1, white -> 2, gray -> 3
tiles = [0] * (MAX + 1)
# 색칠 횟수 카운트 리스트
count = [0] * (MAX + 1)

n = int(input())
start = 0

for _ in range(n):
    length, direction = input().split()
    length = int(length)

    if direction == 'R':
        for i in range(start + OFFSET, start + OFFSET + length):
            if tiles[i] == 3: # 회색인 경우 넘어감
                continue
            count[i] += 1
            tiles[i] = 1
            if count[i] >= 4: # 4번 이상 칠해질 시 회색으로 변경
                tiles[i] = 3
        start += (length - 1)
    else:
        for i in range(start+ OFFSET, start + OFFSET - length, -1):
            if tiles[i] == 3:
                continue
            count[i] += 1
            tiles[i] = 2
            if count[i] >= 4:
                tiles[i] = 3
        start -= (length - 1)


black = 0
white = 0
gray = 0
# 개수 check
for tile in tiles:
    if tile == 1:
        black += 1
    elif tile == 2:
        white += 1
    elif tile == 3:
        gray += 1

print(white, black, gray)