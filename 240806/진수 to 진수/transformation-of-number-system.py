a, b = map(int, input().split())
n = int(input())

# 10진수로 변환
result = 0
count = 0
while n > 0:
    digit = n % 10
    n //= 10
    result += digit * a ** count
    count += 1

digits = []
# b진수로 변환
while True:
    if result < b:
        digits.append(result)
        break
    
    digits.append(result % b)
    result //= b


for d in digits[:: -1]:
    print(d, end="")