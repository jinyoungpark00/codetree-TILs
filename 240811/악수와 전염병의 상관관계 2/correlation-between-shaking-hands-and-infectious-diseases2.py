N, K, P, T = map(int, input().split())

# 감염 리스트
infection = [(0, K)] * (N + 1)
infection[P] = (1, K)

# 악수 리스트
shakes = []

# 악수
for _ in range(T):
    shakes.append(tuple(map(int, input().split())))

# 악수 리스트 정렬
shakes.sort(key=lambda t:t[0])

# 악수 진행
for shake in shakes:
    t, x, y = shake
    is_infected_x, K_x = infection[x]
    is_infected_y, K_y = infection[y]

    if (is_infected_x == 1 and K_x > 0) or (is_infected_y == 1 and K_y > 0):
        if is_infected_x:
            K_x -= 1
        if is_infected_y:
            K_y -= 1
        infection[x] = (1, K_x)
        infection[y] = (1, K_y)

for i in range(1, N + 1):
    print(infection[i][0], end="")