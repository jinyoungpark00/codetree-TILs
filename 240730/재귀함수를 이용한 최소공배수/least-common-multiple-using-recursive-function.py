n = int(input())
array = list(map(int, input().split()))


def max_sub(a, b):
    result = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            result = i
    return result

def min_sub():
    for i in range(0, len(array) - 1):
        pre = array[i]
        now = array[i + 1]
        max_sub_local = max_sub(pre, now)

        if max_sub_local == 1:
            local_result = pre * now
        elif max_sub_local == min(pre, now):
            local_result = min(pre, now)
        else:
            local_result = max_sub_local * min(pre, now)
        
        array[i + 1] = local_result
    
    return array[i]

print(min_sub())