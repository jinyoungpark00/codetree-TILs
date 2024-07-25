n = int(input())
array = list(map(int, input().split()))

def make_plus(array):
    for i in range(n):
        if array[i] < 0:
            array[i] *= -1

make_plus(array)

for i in array:
    print(i, end=" ")