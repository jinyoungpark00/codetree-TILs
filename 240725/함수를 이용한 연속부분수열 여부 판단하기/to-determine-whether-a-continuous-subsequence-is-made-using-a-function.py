n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_fraction(n1, n2):
    for i in range(len(a)):
        if a[i] == b[0]:
            for j in range(1, len(b)):
                if a[i + j] != b[j]:
                    return False
                return True
    return False

if is_fraction(n1, n2):
    print("Yes")
else:
    print("No")