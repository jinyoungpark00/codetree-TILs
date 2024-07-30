n = int(input())
array = list(map(int, input().split()))

sorted_array = sorted(array)
sorted_array_reverse = list(reversed(sorted_array))

for i in sorted_array:
    print(i, end=" ")
print()
for i in sorted_array_reverse:
    print(i, end=" ")