n, m = map(int, input().split())

def maxi(n, m):
    for i in range(max(n, m) + 1, 1, -1):
        if n % i == 0 and m % i == 0:
            return i

print(maxi(n, m))