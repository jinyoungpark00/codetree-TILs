class Person():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def print_info(self):
        print(self.name, self.height, self.weight)

person_list = []
n = int(input())
for _ in range(n):
    name, height, weight = input().split()
    person_list.append(Person(name, height, weight))

person_list.sort(key=lambda person: person.height)

for i in range(n):
    person_list[i].print_info()