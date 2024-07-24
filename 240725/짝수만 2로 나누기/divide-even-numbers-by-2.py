n = int(input())
array = list(map(int, input().split()))

def divide_by_2(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] //= 2

divide_by_2(array)

for i in array:
    print(i, end=" ")