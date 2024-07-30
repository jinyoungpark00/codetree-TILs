n, k, st = input().split()
n = int(n)
k = int(k)
array = []
special_array = []

for _ in range(n):
    array.append(input())

for string in array:
    if st in string:
        special_array.append(string)

sorted_special_array = sorted(special_array)

print(sorted_special_array[k - 1])