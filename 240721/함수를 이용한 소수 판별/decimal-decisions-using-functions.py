a, b = map(int, input().split())

def prime_sum(a, b):
    result = 0
    for i in range(a, b + 1):
        if is_prime(i):
            result += i
    return result

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

print(prime_sum(a, b))