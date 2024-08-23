n, k = map(int, input().split())
# 점수 표시 array
array = [0] * 10001
for _ in range(n):
    index, alpha = input().split()
    index = int(index)
    # 해당 인덱스에 점수 기입
    if alpha == 'G':
        array[index] = 1
    elif alpha == 'H':
        array[index] = 2

# 점수 계산
ans = 0
for i in range(1, 10001 - k):
    local = 0
    for j in range(i, i + k + 1):
        local += array[j]
    # 최대 점수 갱신
    ans = max(ans, local)

print(ans)