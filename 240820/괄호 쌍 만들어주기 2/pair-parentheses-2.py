s = input()
n = len(s)

# 완전 탐색
count = 0
for i in range(n - 3):
    if s[i] == '(' and s[i + 1] == '(':
        for j in range(i + 2, n - 1):
            if s[j] == ')' and s[j + 1] == ')':
                count += 1

print(count)