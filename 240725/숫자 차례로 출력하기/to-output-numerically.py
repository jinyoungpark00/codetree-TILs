n = int(input())

def print_ac(n):
    if n == 0:
        return
    
    print_ac(n - 1)
    print(n, end=" ")

def print_dec(n):
    if n == 0:
        return
    
    print(n, end=" ")
    print_dec(n - 1)

print_ac(n)
print()
print_dec(n)