n, k = map(int, input().split())
array = list(map(int, input().split()))

ans = 0
for i in range(n - k + 1):
    local = 0
    for j in range(i, i + k):
        local += array[j]
    ans = max(ans, local)

print(ans)