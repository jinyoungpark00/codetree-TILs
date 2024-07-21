n = int(input())

def is_magic_num(n):
    one = n % 10
    ten = n // 10
    check = one + ten
    if n % 2 == 0 and check % 5 == 0:
        return "Yes"
    else:
        return "No"

print(is_magic_num(n))