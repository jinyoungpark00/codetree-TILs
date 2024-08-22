n = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 전역검사
total = 0
for i in range(n):
    for j in range(n):
        if not in_range(i, j + 2):
            continue
        # 같은 열 탐색
        for k in range(j + 3, n):
            if not in_range(i, k + 2):
                continue
            print(i, k)
            total = max(total, matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]
                                + matrix[i][k] + matrix[i][k + 1] + matrix[i][k + 2])
        # 다른 열 탐색
        for k in range(i + 1, n):
            for l in range(n):
                if not in_range(k, l + 2):
                    continue
                total = max(total, matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]
                                    + matrix[k][l] + matrix[k][l + 1] + matrix[k][l + 2])

print(total)