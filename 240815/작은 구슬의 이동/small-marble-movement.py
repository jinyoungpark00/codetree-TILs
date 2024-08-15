n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 남 동 서 북
dr, dc = [1, 0, 0, -1], [0, 1, -1, 0]

# 방향 매핑
direc = {
    'D': 0,
    'R': 1,
    'L': 2,
    'U': 3
}

d = direc[d]

# 범위 체크
def in_range(r, c):
    return 1 <= r and r < n and 1 <= c and c < n


# 시뮬레이션
for _ in range(t):
    nr, nc = r + dr[d], c + dc[d]
    # 벽에 닿았을 경우
    if not in_range(nr, nc):
        d = 3 - d
    else:
        r, c = nr, nc

print(r, c)