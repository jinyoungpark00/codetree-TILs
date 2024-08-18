s = input()

count = 0
for i in range(len(s)):
    if s[i] == '(':
        for j in range(i + 1, len(s)):
            if s[j] == ')':
                count += 1

print(count)