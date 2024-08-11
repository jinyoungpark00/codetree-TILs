n = int(input())

x, y = 0, 0
# 서 남 북 동
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def move(direction, dist):
    global x, y
    if direction == 'W':
        x += (dx[0] * dist)
        y += (dy[0] * dist)
    elif direction == 'S':
        x += (dx[1] * dist)
        y += (dy[1] * dist)
    elif direction == 'N':
        x += (dx[2] * dist)
        y += (dy[2] * dist)
    elif direction == 'E':
        x += (dx[3] * dist)
        y += (dy[3] * dist)

for _ in range(n):
    direction, dist = input().split()
    dist = int(dist)
    move(direction, dist)

print(x, y)