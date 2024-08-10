n, m = map(int, input().split())

# 명령어 저장
inst_n = []
inst_m = []
for _ in range(n):
    direction, distance = input().split()
    inst_n.append((direction, int(distance)))

for _ in range(m):
    direction, distance = input().split()
    inst_m.append((direction, int(distance)))

# 총 이동 거리
total_distance = 0
for inst in inst_n:
    direction, distance = inst
    total_distance += distance

# 위치 리스트
location_n = [0] * (total_distance + 1)
location_m = [0] * (total_distance + 1)

# 이동 시뮬레이션
loc = 0
start = 1
for inst in inst_n:
    direction, distance = inst
    for i in range(start, distance + start):
        if direction == 'R':
            loc += 1
            location_n[i] = loc
        else:
            loc -= 1
            location_n[i] = loc
    start += distance

loc = 0
start = 1
for inst in inst_m:
    direction, distance = inst
    for i in range(start, distance + start):
        if direction == 'R':
            loc += 1
            location_m[i] = loc
        else:
            loc -= 1
            location_m[i] = loc
    start += distance

# 비교
for i in range(1, total_distance + 1):
    if location_n[i] == location_m[i]:
        print(i)
        break
    elif i == total_distance:
        print(-1)