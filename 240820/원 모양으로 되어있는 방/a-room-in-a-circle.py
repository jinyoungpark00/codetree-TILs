n = int(input())

# 인원 수 입력
room = [
    int(input())
    for _ in range(n)
]

# 최소 거리 탐색
ans = int(1e9)
for i in range(n):
    count = 0
    dist = 0
    for j in range(i + 1, n + i):
        count += 1
        j %= n
        dist += room[j] * count
    ans = min(ans, dist)

print(ans)