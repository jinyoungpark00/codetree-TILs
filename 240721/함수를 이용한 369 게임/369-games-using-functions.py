a, b = map(int, input().split())

def is_magic_num(a, b):
    count = 0
    for i in range(a, b + 1):
        if i % 3 == 0 or is369(str(i)):
            count += 1
    return count

def is369(i):
    if '3' in i or '6' in i or '9' in i:
        return True
    else:
        return False

print(is_magic_num(a, b))