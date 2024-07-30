n = int(input())
array = []
for _ in range(n):
    array.append(input())

array.sort()

for item in array:
    print(item)