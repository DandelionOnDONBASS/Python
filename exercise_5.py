cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' or 'onions' in requested_toppings:
    print('Yes')
else:
    print('No')

banned_users = ['andrew', 'carolina', 'david']
user = 'John'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
#Упражнение 5.1
cars = ['subaru','audi']
car = 'udi'
if car == 'subaru':
    print('True')
elif car == 'audi':
    print('this is audi')
else:
    print('No car in tshi range')

#Упражнение 5.2
qwerty=[1,2,4,7,'car','beer','apple']
st=[]
cf=[]
for i in qwerty:
    if (type(i) == str) and len(i)>3:
        st.append(i)
    elif type(i)==int:
        cf.append(i)
print(len(st),st)
print(len(cf),cf)


age = 12
if age >= 18:
    print("You are old enough to vote!")
else:
    print('More')


age = 13
if age<5:
    price = 0
elif age <16:
    price =5
else:
    price = 10
print(f'Your addmission cost is ${price}.')

#Упражнение 5.3
alien_color = 'green'
if alien_color == 'green':
    print('You win 5$')

alien_color='green'
if alien_color == 'red':
    print('You win 5$')

#Упражнение 5.4
alien_color = 'red'
if alien_color == 'green':
    print('you win 5$')
elif alien_color == 'red':
    print("You win 10$")

alien_color = 'green'
if alien_color == 'green':
    print('you win 5$')
elif alien_color == 'red':
    print("You win 10$")

alien_color = 'yellow'
if alien_color == 'green':
    print('you win 5$')
elif alien_color == 'red':
    print("You win 10$")
else:
    print('You win 15$')

    
age = 12
if age<2:
    print("Младенец")
elif age <=4:
    print("малыш")
elif age<=13:
    print('Ребенок')
elif age <=20:
    print("Подросток")
elif age<=65:
    print('Взрослый')
else:
    print('Пожилой человек')

#Упражнение 5.7
favorite_fruits = ['Orange','Banana','Kivi','Apple','Potata']
if 'Orange' in favorite_fruits:
    print('You really like Orange!')
if 'pivo' in favorite_fruits:
    print('You really like Pivo!')
if 'Kivi' in favorite_fruits:
    print('You really like Kivi!')



