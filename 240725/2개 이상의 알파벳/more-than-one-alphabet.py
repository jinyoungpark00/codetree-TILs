a = input()

def is_over_two(a):
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            return True
    return False

if is_over_two(a):
    print("Yes")
else:
    print("No")