matrix = [
    list(map(int, input().split()))
    for _ in range(19)
]

# 방향을 위한 배열 (우측, 하단, 우하단 대각선, 좌하단 대각선)
directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

def check_winner():
    for r in range(19):
        for c in range(19):
            if matrix[r][c] != 0:
                color = matrix[r][c]
                for dr, dc in directions:
                    count = 1
                    nr, nc = r + dr, c + dc
                    while 0 <= nr < 19 and 0 <= nc < 19 and matrix[nr][nc] == color:
                        count += 1
                        if count == 5:
                            # 육목이 아닌지 확인 (양 끝에 같은 색이 없어야 함)
                            prev_r, prev_c = r - dr, c - dc
                            next_r, next_c = nr + dr, nc + dc
                            if (not (0 <= prev_r < 19 and 0 <= prev_c < 19) or matrix[prev_r][prev_c] != color) and \
                               (not (0 <= next_r < 19 and 0 <= next_c < 19) or matrix[next_r][next_c] != color):
                                # 가운데 돌 출력 (가로세로 대각선에 따라 다름)
                                mid_r, mid_c = r + (dr * 2), c + (dc * 2)
                                return color, mid_r + 1, mid_c + 1
                        nr += dr
                        nc += dc
    return 0, 0, 0

winner, x, y = check_winner()

if winner:
    print(winner)
    print(x, y)
else:
    print(0)