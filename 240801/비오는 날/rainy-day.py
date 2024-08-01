class Forcast():
    def __init__(self, day, week, weather):
        self.day = day
        self.week = week
        self.weather = weather

forcast_list = []
n = int(input())
for _ in range(n):
    day, week, weather = input().split()
    forcast_list.append(Forcast(day, week, weather))

forcast_list.sort(key=lambda forcast: forcast.day)

for forcast in forcast_list:
    if forcast.weather == "Rain":
        print(forcast.day, forcast.week, forcast.weather)
        break