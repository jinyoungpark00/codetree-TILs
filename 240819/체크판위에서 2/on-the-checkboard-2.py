def count_ways_to_jump(r, c, matrix):
    def dfs(x, y, jump_count, last_color):
        # 만약 점프가 3번 일어났다면
        if jump_count == 3:
            # 도착 지점에 도착했는지 확인
            return 1 if (x == r-1 and y == c-1) else 0
        
        # 경우의 수 카운트
        count = 0
        
        # 다음 점프는 오른쪽과 아래로 최소 한 칸 이상 이동해야 함
        for i in range(x + 1, r):
            for j in range(y + 1, c):
                # 색상이 달라야만 점프 가능
                if matrix[i][j] != last_color:
                    # 다음 점프 진행
                    count += dfs(i, j, jump_count + 1, matrix[i][j])
        
        return count

    # 첫 번째 점프는 시작점 (0, 0)에서 시작, 첫 번째 색은 matrix[0][0]
    return dfs(0, 0, 0, matrix[0][0])

# 입력 처리
r, c = map(int, input().split())
matrix = [input().split() for _ in range(r)]

# 결과 출력
print(count_ways_to_jump(r, c, matrix))