dev = list(map(int, input().split()))

def get_diff(i, j, k):
    team1 = dev[i] + dev[j] + dev[k]
    team2 = sum(dev) - team1
    return abs(team1 - team2)

ans = int(1e9)
for i in range(4):
    for j in range(i + 1, 5):
        for k in range(j + 1, 6):
            diff = get_diff(i, j, k)
        ans = min(ans, diff)

print(ans)