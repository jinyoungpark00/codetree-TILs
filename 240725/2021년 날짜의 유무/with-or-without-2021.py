m, d = map(int, input().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_valid(m, d):
    if m < 1 or m > 12:
        return False
    
    mon = month[m]
    if d > mon:
        return False
    else:
        return True

if is_valid(m, d):
    print("Yes")
else:
    print("No")