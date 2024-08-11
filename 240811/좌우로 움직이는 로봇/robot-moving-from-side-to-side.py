MAX = 1000000

n, m = map(int, input().split())
robot_a = [0] * (MAX + 1)
robot_b = [0] * (MAX + 1)


# 로봇 A 이동
start = 1
v = 0
for _ in range(n):
    t, d = input().split()
    t = int(t)
    for i in range(start, start + t):
        v = v + 1 if d == 'R' else v - 1
        robot_a[i] = v
    start += t
    MAX = min(MAX, start)

# 로봇 B 이동
start = 1
v = 0
for _ in range(m):
    t, d = input().split()
    t = int(t)
    for i in range(start, start + t):
        v = v + 1 if d == 'R' else v - 1
        robot_b[i] = v
    start += t
    MAX = min(MAX, start)

# 마주치는 경우 count
count = 0
for i in range(1, MAX + 1):
    if (robot_a[i - 1] != robot_b[i - 1]) and (robot_a[i] == robot_b[i]):
        count += 1

print(count)