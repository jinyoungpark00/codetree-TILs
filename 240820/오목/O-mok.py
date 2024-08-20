matrix = [
    list(map(int, input().split()))
    for _ in range(19)
]


def check_winner(r, c):
    if matrix[r][c] == 0:
        return (0, 0, 0)
    # 모든 방향 승리 조건 check
    if r - 2 >= 0 and r + 2 <= 18 and c - 2 >= 0 and c + 2 <= 18:
        d1, d2, d3, d4 = False, False, False, False
        for i in range(-2, 2):
            if matrix[r + i][c] != matrix[r + i + 1][c]:
                d1 = True
            if matrix[r][c + i] != matrix[r][c + i + 1]:
                d2 = True
            if matrix[r + i][c + i] != matrix[r + i + 1][c + i + 1]:
                d3 = True
            if matrix[r - i][c + i] != matrix[r - i - 1][c + i + 1]:
                d4 = True
        if d1 == False or d2 == False or d3 == False or d4 == False:
            return (matrix[r][c], r + 1, c + 1)
        else:
            return (0, 0, 0)
    return (0, 0, 0)
            
            

winner = (0, 0, 0)
found_winner = False

for i in range(19):
    if found_winner:
        break
    for j in range(19):
        winner = check_winner(i, j)
        if winner[0] != 0:
            found_winner = True  # 승자를 찾았음을 기록
            break  # 내부 루프 탈출
            
            
if winner[0] != 0:
    print(winner[0])
    print(winner[1], winner[2])
else:
    print(0)