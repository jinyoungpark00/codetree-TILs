n, k = map(int, input().split())
array = list(map(int, input().split()))

count = 1
max_count = 1
for i in range(n):
    if i == 0 or array[i] < k or array[i - 1] >= array[i]:
        count = 1
    elif array[i - 1] > k:
        count += 1
    max_count = max(max_count, count)

print(max_count)