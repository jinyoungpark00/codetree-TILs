n = int(input())
string = []
while True:
    if n < 2:
        string.append(n)
        break
    
    string.append(n % 2)
    n = n // 2

for binary in string[:: -1]:
    print(binary, end="")