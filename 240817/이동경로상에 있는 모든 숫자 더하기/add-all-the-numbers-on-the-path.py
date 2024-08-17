n, k = map(int, input().split())
insts = input()

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

visited = [
    [False] * n
    for _ in range(n)
]

# R D L U
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
# 시작 방향 (U)
d = 3
# 시작 위치 (정중앙)
x, y = n // 2, n // 2
# 방문 처리
visited[x][y] = True
# score
score = matrix[x][y]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 시뮬레이션
for inst in insts:
    if inst == 'R':
        d = (d + 1) % 4
    elif inst == 'L':
        d = (d + 3) % 4
    elif inst == 'F':
        nx, ny = x + dx[d], y + dy[d]
        # 범위를 벗어날 경우 명령어 무시
        if not in_range(nx, ny):
            continue
        # 이동
        x, y = nx, ny
        # 방문하지 않은 곳이라면 점수 count
        if visited[x][y] == False:
            score += matrix[x][y]

# 출력
print(score)