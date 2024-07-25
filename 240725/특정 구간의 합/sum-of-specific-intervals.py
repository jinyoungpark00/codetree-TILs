n, m = map(int, input().split())
array = list(map(int, input().split()))

def print_sum():
    for _ in range(m):
        a, b = map(int, input().split())
        result = sum(array[a - 1: b])
        print(result)

print_sum()