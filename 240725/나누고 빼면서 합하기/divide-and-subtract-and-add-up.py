n, m = map(int, input().split())
array = list(map(int, input().split()))

def while_m_is_1():
    global m
    result = array[m - 1]
    while m > 1:
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
        
        result += array[m - 1]
    return result

result = while_m_is_1()

print(result)