y = int(input())

def yun(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True

if yun(y):
    print("true")
else:
    print("false")