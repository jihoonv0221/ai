trolly = ['김광석CD', '아이폰15 프로']
print(trolly)
food = ['다시마', '멸치']
trolly.append(food)
print(trolly)
print(trolly[2][1])
#print(trolly.pop()) # 리스트의 맨 마지막 원소를 리턴 후 삭제
#print(trolly[2].pop()) # 멸치 원소를 리턴 후 삭제
print(trolly[2].pop(0)) # 다시마 원소를 리턴 후 삭제
print(trolly)
# trolly.append('다시마')
trolly[2].append('다시마')
print(trolly)
trolly[2].insert(0, '딸기')
print(trolly)

# trolly[1:2] = '아이폰 15' # ['김광석CD', '아', '이', '폰', ' ', '1', '5', ['딸기', '멸치', '다시마']]

trolly[1:2] = ['아이폰 15'] #아이폰 15 프로 --> 아이폰 15
print(trolly)


#numbers1 = list()
#numbers2 = [-9, 0, 7]
#for i in range(0, 5):
    #numbers1.append(i)
#print(numbers1)
#numbers3 = numbers1 + numbers2
#print(numbers3)
#print(numbers1)
#numbers1.extend(numbers2) # numbers1 = numbers1 + numbers2
#print(numbers1)
