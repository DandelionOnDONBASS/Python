
for value in range(1,6):
    print(value)

num = list(range(6))
print(num)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
squares = [value**2 for value in range(1,11)]
print(squares)

#Упражнение 4.3
for i in range(21):
    print(i)

#Упражнение 4.4
mil =[]
for i in range(1,1000001):
    mil.append(i)
print(mil)

#Упражнение 4.5
mil =[]
for i in range(1,101):
    mil.append(i)
print(max(mil))
print(min(mil))

#Упражнение 4.6
for i in range(1,21,2):
    print(i)
print('\n')

#Упражнение 4.7
for i in range(3,30):
    if i%3==0:
        print(i)
print('\n')

#Упражнение 4.8
for i in range(10):
    print(i**3)
print('\n')
    #Упражнение 4.9
squares = [value**3 for value in range(1,11)]
print(squares)

