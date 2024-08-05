a, b, c = map(int, input().split())

def cal_time(day, hour, minute):
    day -= 11
    hour -= 11
    minute -= 11
    return day * 24 * 60 + hour * 60 + minute

print(cal_time(a, b, c))