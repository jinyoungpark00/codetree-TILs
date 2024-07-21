a, b = map(int, input().split())
count = 0

def is_on(i):
    if i % 2 == 0:
        return False
    elif i % 10 == 5:
        return False
    elif i % 3 == 0 and i % 9 != 0:
        return False
    return True

for i in range(a, b +1):
    if is_on(i):
        count += 1

print(count)