n = int(input())
array = list(map(int, input().split()))

for i in range(0, len(array), 2):
    sub = array[0: i + 1]
    sub.sort()
    print(sub[len(sub) // 2], end=" ") # 중앙값 출력