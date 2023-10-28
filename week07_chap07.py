numbers = list()
for i in range(0, 11):
   #print(i, end=' ')
    numbers.append(i)
print(numbers)
odd_numbers = numbers[1::2]
even_numbers = numbers[::2]
print(odd_numbers)
print(even_numbers)
reverse_odd_numbers = numbers[-2::1-2]
print(reverse_odd_numbers)
reverse_numbers = numbers[::-1]
numbers.reverse()
print(reverse_numbers)
numbers.append(-11)
print(numbers)
numbers.insert(5,99)
print(numbers)
numbers.insert(-2, 55)
print(numbers)
numbers = numbers * 2 # list multiplication
print(numbers)