n, m = map(int, input().split())

# n * m matrix
matrix = [[0] * m for _ in range(n)]
# R D L U
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
# 시작 인덱스 0,0
x, y = 0, 0
# 시작 방향 R
direc = 0
# 시작 인덱스 방문 설정
matrix[x][y] = 1


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 시뮬레이션
for i in range(2, n * m + 1):
    nx, ny = x + dxs[direc], y + dys[direc]
    # 밖으로 나가거나 이미 방문한 인덱스인 경우 방향 전환
    if not in_range(nx, ny) or matrix[nx][ny] != 0:
        direc = (direc + 1) % 4
        nx, ny = x + dxs[direc], y + dys[direc]
    # 인덱스 이동
    x, y = nx, ny
    # 인덱스 번호 설정
    matrix[x][y] = i


# 출력
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()