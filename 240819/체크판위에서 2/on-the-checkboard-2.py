r, c = map(int, input().split())
m = [
    list(input().split())
    for _ in range(r)
]

r, c = r - 1, c - 1
sr, sc = 0, 0
flag = m[sr][sc]

# 탐색 시뮬레이션
count = 0
for i in range(sr + 1, r):
    for j in range(sc + 1, c):
        # 첫 번째 jump
        if m[i][j] != flag:
            flag = m[i][j]
            for k in range(i + 1, r):
                for l in range(j + 1, c):
                    # 두 번째 jump
                    if m[k][l] != flag:
                        if k < r and l < c:
                            count += 1
                        
if m[sr][sc] == m[r][c]:
    print(0)
else:
    print(count)