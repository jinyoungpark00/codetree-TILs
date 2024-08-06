n = int(input())
result = 0
count = 0
while n > 0:
    digit = n % 10
    n //= 10
    result += digit * 2 ** count
    count += 1

print(result)