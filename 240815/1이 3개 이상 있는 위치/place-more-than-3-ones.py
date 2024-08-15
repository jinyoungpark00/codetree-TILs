n = int(input())
matrix = []

# 동 남 서 북
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

# 배열 입력
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 범위 check
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 인접 1 count
def count_adj_one(x, y):
    local_count = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and matrix[nx][ny] == 1:
            local_count +=1
    return local_count

# 시뮬레이션
count = 0
for x in range(n):
    for y in range(n):
        if count_adj_one(x, y) >= 3:
            count += 1

print(count)