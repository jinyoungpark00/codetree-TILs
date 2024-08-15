# 북, 동, 남, 서
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
direc = 0
x, y = 0, 0

insts = input()

for inst in insts:
    if inst == 'L':
        direc = (direc + 3) % 4
    elif inst == 'R':
        direc = (direc + 1) % 4
    else:
        x, y = x + dx[direc], y + dy[direc]

print(x, y)