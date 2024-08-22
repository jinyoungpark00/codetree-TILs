n, m = map(int, input().split())
words = [
    input()
    for _ in range(n)
]

# 8방향 정의
dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 전역 검사
count = 0
for i in range(n):
    for j in range(m):
        # L 로 시작하는 경우만 검사
        if words[i][j] == 'L':
            # 8방향 검사
            for dx, dy in zip(dxs, dys):
                nx = i + dx * 2
                ny = j + dy * 2

                # 범위 검사
                if not in_range(nx, ny):
                    continue
                # E E 가 이어서 오는지 검사
                if words[nx - dx][ny - dy] == words[nx][ny] == 'E':
                    count += 1

print(count)