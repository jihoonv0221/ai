student_id = 1000
student_name = "류지훈"
subject = ["파이썬", "통계학", "수학"]
score = 3.7


print(f"학번이 {student_id}인 {student_name} 학생은(는) {subject}을 수강하였고 학점이 {score}입니다")
print(type(student_id), type(student_name), type(subject), type(score))
print(id(student_id), id(student_name), id(subject), id(score))

if False: #boolean
    print("무조건 출력 안됩니다")