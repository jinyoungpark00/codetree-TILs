n = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]
sum_list = []

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 전역검사
for i in range(n):
    for j in range(n):
        if not in_range(i, j + 2):
            continue
        sum_list.append(matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2])

sum_list.sort()
first = sum_list.pop()
second = sum_list.pop()
print(first+ second)