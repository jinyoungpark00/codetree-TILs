n, k, st = input().split()
n = int(n)
k = int(k)
array = []
special_array = []

for _ in range(n):
    array.append(input())

def is_string_in_array(string):
    for i in range(len(st)):
        char_st = st[i]
        char_string = string[i]
        if char_st != char_string:
            return False
    return True


for string in array:
    if is_string_in_array(string):
        special_array.append(string)

sorted_special_array = sorted(special_array)
print(sorted_special_array[k - 1])