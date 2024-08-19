n = int(input())

# 체크포인트 입력
check = []
for _ in range(n):
    check.append(list(map(int, input().split())))

# 모든 경우의 수 계산
min_length = int(1e9)
for i in range(1, n - 1):
    length = 0
    for j in range(len(check) - 1):
        # 뛰어넘을 체크 포인트
        if j == i:
            continue
        # 거리 계산
        if j == i - 1:
            x1, y1 = check[j]
            x2, y2 = check[j + 2]
        else:
            x1, y1 = check[j]
            x2, y2 = check[j + 1]
        length += abs(x1 - x2) + abs(y1 - y2)
    # 최소 거리
    min_length = min(min_length, length)

print(min_length)