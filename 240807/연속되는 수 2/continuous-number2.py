n = int(input())
array = []
count = 0

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    if i == 0 or array[i] != array[i - 1]:
        count += 1

print(count)