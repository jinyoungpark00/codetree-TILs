class Home_info():
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

    def print_info(self):
        print("name", self.name)
        print("addr", self.addr)
        print("city", self.city)

home_info_list = []
n = int(input())

for _ in range(n):
    name, addr, city = input().split()
    home_info_list.append(Home_info(name, addr, city))

home_info_list.sort(key=lambda home: home.name, reverse=True)

home_info_list[0].print_info()