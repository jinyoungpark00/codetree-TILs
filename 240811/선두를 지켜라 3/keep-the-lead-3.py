MAX = 1000000

n, m = map(int, input().split())

dist_a = [0] * (MAX + 1)
dist_b = [0] * (MAX + 1)
owner = [0] * (MAX + 1)

# A 이동
move_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        dist_a[move_a] = dist_a[move_a - 1] + v
        move_a += 1

# B 이동
move_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        dist_b[move_b] = dist_b[move_b - 1] + v
        move_b += 1

# 명예의 전당 
count = 0
for i in range(1, max(move_a, move_b)):
    if dist_a[i] > dist_b[i]:
        owner[i] = 'a'
    elif dist_a[i] < dist_b[i]:
        owner[i] = 'b'
    elif dist_a[i] == dist_b[i]:
        owner[i] = 'ab'
    # 조합 수 count
    if owner[i] != owner[i - 1]:
        count += 1

print(count)