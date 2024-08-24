n, k = map(int, input().split())
array = [0] * 101
for _ in range(n):
    candy, index = map(int, input().split())
    array[index] += candy

if k >= 49:
    print(sum(array))
else:
    ans = 0
    for i in range(k, 100 - k + 1):
        candy_count = 0
        for j in range(i - k, i + k + 1):
            candy_count += array[j]
        ans = max(ans, candy_count)

    print(ans)