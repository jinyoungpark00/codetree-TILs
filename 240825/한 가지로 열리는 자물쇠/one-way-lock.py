n = int(input())
key1, key2, key3 = map(int, input().split())

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if abs(key1 - i) > 2 and abs(key2 - j) > 2 and abs(key3 - k) > 2:
                count += 1

print(n ** 3 - count)