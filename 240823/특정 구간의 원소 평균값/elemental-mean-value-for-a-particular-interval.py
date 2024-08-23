n = int(input())
array = list(map(int, input().split()))

# 전역 탐색
count = 0
for i in range(n):
    for j in range(i, n):
        mean = sum(array[i: j + 1]) // (j + 1)
        if mean in array[i: j + 1]:
            count += 1

print(count)