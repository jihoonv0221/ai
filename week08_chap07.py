import copy
a = [-11, [3, 0], 9]
b = copy.deepcopy(a)  # deep copy

print(a,b)
a[1][0] = 7
print(a,b)  # 깊은 복사 리스트 b는 변하지 않음
