n, m, k = map(int, input().split())

students = [0] * (n + 1)

is_punished = False
for _ in range(m):
    student_num = int(input())
    students[student_num] += 1
    # 벌금 체크
    if students[student_num] >= k:
        print(student_num)
        is_punished = True
        break

if not is_punished:
    print(-1)