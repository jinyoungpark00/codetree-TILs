n, k = map(int, input().split())
block_list = [0] * (n + 1)

# 블럭 쌓기
for _ in range(k):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        block_list[i] += 1

# 최댓값 출력
print(max(block_list))