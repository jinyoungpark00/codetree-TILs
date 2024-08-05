a, b, c = map(int, input().split())

def cal_time(day, hour, minute):
    day -= 11
    hour -= 11
    minute -= 11
    result = day * 24 * 60 + hour * 60 + minute
    
    if result > 0:
        return result
    else:
        return -1

print(cal_time(a, b, c))