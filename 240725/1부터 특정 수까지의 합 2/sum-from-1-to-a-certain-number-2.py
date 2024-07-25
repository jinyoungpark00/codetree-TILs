n = int(input())

def int_sum(n):
    if n == 1:
        return 1
    
    return int_sum(n - 1) + n

print(int_sum(n))