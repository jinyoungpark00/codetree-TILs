n = int(input())

def get_sum(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return get_sum(n - 2) + n

print(get_sum(n))