subjects = (['python', 5], ['java', 9], ['go', 7])
subjects = dict(subjects)

print(subjects['go'])
print(subjects.get('go'))
print(subjects.values())
print(list(subjects.values()))
print(len(subjects))