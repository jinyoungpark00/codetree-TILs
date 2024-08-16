n = int(input())

# E S W N
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
# 방향 매핑
direcs = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}
# 움직인 거리
count = 0
# 시작점
x, y = 0, 0
# 시작점 여부
recome = False

# 시뮬레이션
for i in range(n):
    d, t = input().split()
    t = int(t)
    # 방향 int로 변환
    d = direcs[d]

    # 명령된 움직임 수행
    for j in range(t):
        x, y = x + dxs[d], y + dys[d]
        count += 1
        # 되돌아온 경우 종료
        if x == 0 and y == 0:
            print(count)
            recome = True
            break
    
    if recome:
        break

if not recome:
    print(-1)