n = int(input())
result = 0
count = 0

while n > 0:
    digit = n % 10
    n //= 10
    result += digit * 2 ** count
    count += 1

result *= 17
digits = []
while True:
    if result < 2:
        digits.append(result)
        break
    
    digits.append(result % 2)
    result //= 2

for digit in digits[:: -1]:
    print(digit, end="")