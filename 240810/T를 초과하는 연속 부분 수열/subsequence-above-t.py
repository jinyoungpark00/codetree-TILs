n, t = map(int, input().split())
array = list(map(int, input().split()))

max_count = 0
count = 0

for i in range(n):
    if array[i] > t:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print(max_count)