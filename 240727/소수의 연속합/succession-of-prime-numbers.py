n = int(input())
count = 0

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(n):
    for i in range(2, n // 2 + 1):
        if is_prime(i):
            n -= i
        if n == 0: