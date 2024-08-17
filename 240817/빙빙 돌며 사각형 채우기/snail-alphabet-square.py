n, m = map(int, input().split())
matrix = [
    [0] * m
    for _ in range(n)
]

# R D L U
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
# 시작 방향 (R)
d = 0
# 시작점
x, y = 0, 0
# 시작 지점 방문 처리
matrix[x][y] = 'A'
# 알파벳 카운트
alpha = 66

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 시뮬레이션
for _ in range(2, n * m + 1):
    nx, ny = x + dx[d], y + dy[d]
    # matrix를 벗어나거나 이미 방문한 인덱스라면 우회전
    if not in_range(nx, ny) or matrix[nx][ny] != 0:
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
    x, y = nx, ny
    # alpha 채워넣기
    matrix[x][y] = chr(alpha)
    # alpha 증가
    alpha += 1
    if alpha > 81:
        alpha -= 26

# 출력
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()