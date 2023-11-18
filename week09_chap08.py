subjects = (['python', 5],['java', 9])
subjects = dict(subjects)

print(subjects)
print(subjects['java'])
subjects['go'] = 7  # add
print(subjects)
subjects['java'] = 8  # update
print(subjects)

for subject in subjects:
    print(subject)

for subject in subjects.keys():
    print(subject)

for subject in subjects.values():
    print(subject)

for subject in subjects.items():
    print(subject)

for subject, students in subjects.items():
    print(subject, students)
    print(f"{subject} 과목을 수강하는 학생의 인원은 {students}입니다.")

del subjects['java']
print(subjects)
