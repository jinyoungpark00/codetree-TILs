n = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_coin = 0
for i in range(n):
    for j in range(n - 2):
        coin = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]
        max_coin = max(max_coin, coin)

print(max_coin)