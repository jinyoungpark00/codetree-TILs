n = int(input())
count = 0

def solution(n):
    global count
    if n == 1:
        return count
    
    if n % 2 == 0:
        count += 1
        return solution(n // 2)
    else:
        count += 1
        return solution(n // 3)

print(solution(n))