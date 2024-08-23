n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


count = 0
for i in range(n - m + 1):
    is_in = 0
    for item in b:
        if item in a[i: i + m]:
            is_in += 1
    if is_in == m:
        count += 1

print(count)