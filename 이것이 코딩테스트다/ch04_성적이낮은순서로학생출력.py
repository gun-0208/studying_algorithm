# n명의 학생정보. 학생정보는 학생이름 학생성적으로 구분.
# 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램 작성.
# 2
# 홍길동 95
# 이순신 77
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],input_data[1]))

array = sorted(array,key=lambda student:student[1])

for student in array:
    print(student[0], end=' ')