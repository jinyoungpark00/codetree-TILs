n = int(input())
blocks = [0] * 101

for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        blocks[i] += 1

print(max(blocks))