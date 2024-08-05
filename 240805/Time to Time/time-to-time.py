a, b, c, d = map(int, input().split())

target = 60 * c + d
current = 60 * a + b

result = target - current
print(result)