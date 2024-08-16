# U R D L [row, col]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
# 이동 count
count = 0
# 되돌아 왔는지 여부
recome = False
# 시작점
x, y = 0, 0
# 북쪽 방향부터 시작
direc = 0

# 시뮬레이션
for inst in input():
    nx, ny = x + dxs[direc], y + dys[direc]
    if inst == 'F':
        x, y = nx, ny
    elif inst == 'L':
        direc = (direc + 3) % 4
    elif inst == 'R':
        direc = (direc + 1) % 4
    # 이동 시간 증가
    count += 1
    # 되돌아 왔는지 여부 체크
    if x == 0 and y == 0:
        print(count)
        recome = True
        break

if not recome:
    print(-1)