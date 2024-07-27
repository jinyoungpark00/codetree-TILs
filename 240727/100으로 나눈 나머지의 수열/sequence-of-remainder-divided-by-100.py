n = int(input())

def get_func(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4

    return (get_func(n - 1) * get_func(n - 2)) % 100

print(get_func(n))