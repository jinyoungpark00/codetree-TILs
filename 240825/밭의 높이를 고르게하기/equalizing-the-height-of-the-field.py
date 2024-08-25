n, h, t = map(int, input().split())
array = list(map(int, input().split()))

ans = int(1e9)
for i in range(n - t + 1):
    count = 0
    for j in range(i, i + t):
        count += abs(array[j] - h)
    ans = min(ans, count)

print(ans)