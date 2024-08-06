n = int(input())
blocks = [0] * (202)

# 선분 배치
for _ in range(n):
    start, end = map(int, input().split())
    start += 100; end += 100
    for i in range(start, end):
        blocks[i] += 1

# 최대로 겹치는 선분 출력
print(max(blocks))