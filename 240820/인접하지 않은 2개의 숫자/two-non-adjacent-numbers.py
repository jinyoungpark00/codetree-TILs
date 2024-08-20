n = int(input())
s = list(map(int, input().split()))

ans = 0
for i in range(n - 2):
    for j in range(i + 2, n):
        v = s[i] + s[j]
        ans = max(ans, v)

print(ans)