a, b = map(int, input().split())
count = 0

def is_so(i):
    if i <= 1:
        return False
    else:
        for j in range(2, i):
            if i % j == 0:
                return False
        return True


def is_even(i):
    count = 0
    while i > 0:
        one = i % 10
        i = i // 10
        count += one
    if count % 2 == 0:
        return True
    else:
        return False


for i in range(a, b + 1):
    if is_so(i) and is_even(i):
        count += 1

print(count)