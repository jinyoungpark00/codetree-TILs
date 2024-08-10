MAX = 1000000

array_n = [0] * (MAX + 1)
array_m = [0] * (MAX + 1)

n, m = map(int, input().split())

# A 이동 기록
start = 1
for _ in range(n):
    v, t = map(int, input().split())
    # 이동
    for i in range(start, start + t):
        array_n[i] += (array_n[i - 1] + v)
    start += t

# B 이동 기록
start = 1
for _ in range(m):
    v, t = map(int, input().split())
    # 이동
    for i in range(start, start + t):
        array_m[i] += (array_m[i - 1] + v)
    start += t


# 선두 계산
count = 0
for i in range(1, start + 1):
     if (array_n[i] > array_m[i] and array_n[i - 1] <= array_m[i - 1]) or \
       (array_n[i] < array_m[i] and array_n[i - 1] >= array_m[i - 1]):
        count += 1

print(count - 1)