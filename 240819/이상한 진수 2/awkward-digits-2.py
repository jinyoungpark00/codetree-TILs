n = input()
n = list(n)

for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        break
n = n[:: -1]

result = 0
for i in range(len(n)):
    result += int(n[i]) * 2 ** i

print(result)