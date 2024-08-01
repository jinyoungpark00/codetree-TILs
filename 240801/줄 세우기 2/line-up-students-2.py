class Student():
    def __init__(self, height, weight, id):
        self.height = height
        self.weight = weight
        self.id = id

student_list = []
n = int(input())
for i in range(1, n + 1):
    h, w = map(int, input().split())
    student_list.append(Student(h, w, i))

student_list.sort(key = lambda student: (student.height, -student.weight))

for student in student_list:
    print(student.height, student.weight, student.id)