n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
for i in range(0, n):
    result = max(result, array[i] + array[-(i + 1)])

print(result)