n = input()
n = list(n)

one_count = 0
for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        break
    one_count += 1

n = n[:: -1]

result = 0
for i in range(len(n)):
    result += int(n[i]) * 2 ** i

if one_count == len(n):
    print(result -1)
else:
    print(result)