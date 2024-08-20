n = int(input())
s = [
    int(input())
    for _ in range(n)
]

def check_carry(f, sk, t):
    flag = False
    for _ in range(5):
        if f < 0 and sk < 0 and t < 0:
            break
        f_, sk_, t_ = f % 10, sk % 10, t % 10
        f, sk, t = f // 10, sk // 10, t // 10
        if f_ + sk_ + t_ > 10:
            flag = True
            break
    return flag

# 모든 조합 탐색
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # fisrt, second, third
            f, sk, t = s[i], s[j], s[k]
            # carry 여부 검사
            flag = check_carry(f, sk, t)
            # carry가 없을 경우에만 합산
            if flag == False:
                total = s[i] + s[j] + s[k]
                ans = max(ans, total)

print(ans)