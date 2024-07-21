a, o, c = input().split()

a = int(a)
c = int(c)

def plus(a, c):
    return a + c

def minus(a, c):
    return a - c

def mult(a, c):
    return a * c

def div(a, c):
    return a // c

result = 0

if o == '+':
    result = plus(a, c)
elif o == '-':
    result = minus(a, c)
elif o == '*':
    result = mult(a, c)
elif o == '/':
    result = div(a, c)

print(f"{a} {o} {c} = {result}")