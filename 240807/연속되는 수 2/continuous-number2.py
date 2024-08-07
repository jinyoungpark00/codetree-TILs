n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

count = 1
max_count = 1
for i in range(n):
    if i == 0 or array[i] != array[i - 1]:
        max_count = max(max_count, count)
        count = 1
    else:
        count += 1
max_count = max(max_count, count)

print(max_count)