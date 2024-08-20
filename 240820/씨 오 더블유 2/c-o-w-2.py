n = int(input())
s = input()

count = 0
for i in range(n):
    if s[i] == 'C':
        for j in range(i + 1, n):
            if s[j] == 'O':
                for k in range(j + 1, n):
                    if s[k] == 'W':
                        count += 1

print(count)