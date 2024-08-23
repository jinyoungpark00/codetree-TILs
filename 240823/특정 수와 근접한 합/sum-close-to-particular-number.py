n, s = map(int, input().split())
array = list(map(int, input().split()))
total = sum(array)

# 전역검사 수행
ans = int(1e9)
for i in range(n - 1):
    for j in range(i, n):
        local_sum = total - array[i] - array[j]
        ans = min(ans, abs(s - local_sum))

print(ans)