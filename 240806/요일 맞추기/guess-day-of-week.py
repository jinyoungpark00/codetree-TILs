m1, d1, m2, d2 = map(int, input().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def check_count(mon, day):
    count = 0
    mon -= 1
    while mon > 0:
        count += month[mon]
        mon -= 1
    count += day
    return count

diff = (check_count(m2, d2) - check_count(m1, d1)) % 7
print(week[diff])