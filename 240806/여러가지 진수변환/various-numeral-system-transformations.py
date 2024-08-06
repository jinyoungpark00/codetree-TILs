n, b = map(int, input().split())
string = []

while True:
    if n < b:
        string.append(n)
        break
    
    string.append(n % b)
    n //= b

for digit in string[:: -1]:
    print(digit, end="")