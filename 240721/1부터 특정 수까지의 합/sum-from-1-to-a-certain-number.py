n = int(input())

def sum_div(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return int(result / 10)

print(sum_div(n))