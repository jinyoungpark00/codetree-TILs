n, m = map(int, input().split())

# matrix (n * m)
matrix = [[0] * m for _ in range(n)]

# D R U L
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
# 시작 방향 (D)
d = 0
# 시작 위치
x, y = 0, 0
# 시작점 방문
matrix[x][y] = 1


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


for i in range(2, n * m + 1):
    nx, ny = x + dxs[d], y + dys[d]
    # matrix 벗어나거나 이미 방문한 경우 좌회전
    if not in_range(nx, ny) or matrix[nx][ny] != 0:
        d = (d + 1) % 4
        nx, ny = x + dxs[d], y + dys[d]
    # 인덱스 이동
    x, y = nx, ny
    matrix[x][y] = i

# 출력
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()