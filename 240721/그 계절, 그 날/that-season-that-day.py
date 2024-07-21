y, m, d = map(int, input().split())

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoon_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isyoon(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def isvalid(isyoon, m, d):
    if isyoon:
        day = yoon_date[m - 1]
        if d >= 1 and d <= day:
            return True
        else:
            return False
    else:
        day = date[m - 1]
        if d >= 1 and d <= day:
            return True
        else:
            return False

def print_season(m):
    if m >= 3 and m <= 5:
        print("Spring")
    elif m >= 6 and m <= 8:
        print("Summer")
    elif m >= 9 and m <= 11:
        print("Fall")
    elif m >= 12 or m <= 2:
        print("Winter")

if isvalid(isyoon(y), m, d):
    print_season(m)
else:
    print(-1)