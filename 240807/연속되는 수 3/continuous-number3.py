n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))


def is_positive(x):
    if x > 0:
        return True
    else:
        return False


count = 1
max_count = 1
for i in range(n):
    if i == 0 or is_positive(array[i]) != is_positive(array[i - 1]):
        count = 1
    else:
        count += 1
    max_count = max(max_count, count)

print(max_count)