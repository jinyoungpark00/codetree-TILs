n, m = map(int, input().split())

def minmult(n, m):
    for i in range(max(n, m), (n * m) + 1):
        if i % n == 0 and i % m == 0:
            return i

print(minmult(n, m))