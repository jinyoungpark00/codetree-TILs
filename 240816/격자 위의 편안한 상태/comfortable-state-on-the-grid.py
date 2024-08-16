n, m = map(int, input().split())

# n * n matrix
matrix = [[0] * n for _ in range(n)]

# row, col -> R D L U
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 시뮬레이션
for _ in range(m):
    x, y = map(int, input().split())
    # 인덱스로 변경
    x, y = x - 1, y - 1
    # 해당 격자 색칠
    matrix[x][y] = 1
    
    count = 0
    # 편안한 상태인지 확인
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if in_range(nx, ny) and matrix[nx][ny] == 1:
            count += 1
    
    if count == 3:
        print(1)
    else:
        print(0)