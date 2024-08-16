n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input()))

k = int(input())

# D L U R [row, col]
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
# 초기 위치와 방향 설정
if 1 <= k <= n:
    x, y, d = 0, k - 1, 0  # 위에서 아래로 (D)
elif n < k <= 2 * n:
    x, y, d = k - n - 1, n - 1, 1  # 오른쪽에서 왼쪽으로 (L)
elif 2 * n < k <= 3 * n:
    x, y, d = n - 1, 3 * n - k, 2  # 아래에서 위로 (U)
elif 3 * n < k <= 4 * n:
    x, y, d = 4 * n - k, 0, 3  # 왼쪽에서 오른쪽으로 (R)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

count = 1
while(in_range(x, y)):
    count += 1
    if (matrix[x][y] == '/' and (d == 3 or d == 1)) or (matrix[x][y] == '\\' and (d == 2 or d == 0)):
        d = (d + 1) % 4
    elif (matrix[x][y] == '/' and (d == 2 or d == 0)) or (matrix[x][y] == '\\' and (d == 3 or d == 1)):
        d = (d + 3) % 4
    x, y = x + dxs[d], y + dys[d]

print(count)