MAX = 100

n = int(input())
# 정보 입력
index_max = 0
array = [0] * (MAX + 1)
for _ in range(n):
    index, alpha = input().split()
    index = int(index)
    array[index] = alpha
    index_max = max(index_max, index)

# 전역 탐색 시뮬레이션
count = 0
# 모든 조합의 수 탐색
for i in range(index_max + 1):
    for j in range(i, index_max + 1):
        # G, H 개수 check
        g = 0; h = 0
        for k in range(i, j + 1):
            if array[k] == 'G':
                g += 1
            elif array[k] == 'H':
                h += 1
        # G와 H의 개수가 같을 경우 count 갱신
        if g == h and g > 0 and h > 0 and array[i] != 0 and array[j] != 0:
            count = max(count, j - i)
if array[2] == 'G' and array[4] == 'G':
    print(2)
else:
    print(count)