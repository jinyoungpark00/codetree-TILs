m1, d1, m2, d2 = map(int, input().split())
target = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def trans_to_day(mon, day):
    days = 0
    for i in range(1, mon):
        days += month[i]
    days += day
    return days

diff = trans_to_day(m2, d2) - trans_to_day(m1, d1)
count = 0
count += (diff // 7)
if week.index(target) <= diff % 7:
    count += 1

print(count)