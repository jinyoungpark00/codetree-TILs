n, k = map(int, input().split())
array = [0] * 101
for _ in range(n):
    candy, index = map(int, input().split())
    array[index] += candy

ans = 0
for i in range(100 - 2 * k):
    candy_count = 0
    for j in range(i, i + 2 * k + 1):
        candy_count += array[j]
    ans = max(ans, candy_count)

print(ans)