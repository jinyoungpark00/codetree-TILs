MAX = 2000
OFFSET = 1000
start = 0

sector = [0] * (MAX + 1)

n = int(input())
for _ in range(n):
    length, direction = input().split()
    length = int(length)
    # 오른쪽 이동
    if direction == 'R':
        for i in range(start + OFFSET, start + OFFSET + length):
            sector[i] += 1
        start += length
    else:
        for i in range(start + OFFSET - length, start + OFFSET):
            sector[i] += 1
        start -= length

count = 0
for i in sector:
    if i >= 2:
        count += 1

print(count)