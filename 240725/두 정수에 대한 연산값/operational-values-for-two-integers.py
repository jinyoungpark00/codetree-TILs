a, b = map(int, input().split())

def cal(a, b):
    if a > b:
        return a + 25, b * 2
    else:
        return a * 2, b + 25

a, b = cal(a, b)
print(a, b)