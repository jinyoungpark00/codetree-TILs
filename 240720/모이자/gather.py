n = int(input())
s = list(map(int, input().split()))

result = int(1e9)

for i in range(n):
    distance_sum = 0
    for j in range(n):
        dist = abs(i - j)
        distance_sum += s[j] * dist
    
    result = min(result, distance_sum)

print(result)