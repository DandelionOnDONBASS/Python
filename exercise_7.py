prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print('\nYou"r tall enough to ride!')
else:
    print('\nYou"ll be able to ride when you"re a little older.')

#Упражнение 7.1

car = 'What car would you like to buy?'
car_1 = input(car)
print(f'let me see if I can fild you a {car_1.title()}' )
#Упражнение 7.2
qwes = 'How many people would you like to book a table for?'
people = int(input(qwes))
if people>8:
    print('you have to wait, we are looking for a table for you')
else:
    print('Come sit down')
#Упражнение 7.3
qwes = "enter the number"
num = int(input(qwes))
if num %10 ==0:
    print(f'{num} multiple of 10')
else:
    print(f'{num} not a multiple of 10')

num = 1
while num<=5:
    print(num)
    num+=1
print('\n')

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)
    print(message)

message = ""
while message!= "quit":
    message=input("\nTell me something, and I will repeat it back to you:\nEnter 'quit' to end the program.")
    #print(message)
    if message != "quit":
        print(message)


active = True
while active:
    message = input("\nTell me something, and I will repeat it back to you:\nEnter 'quit' to end the program.")
    if message =="quit":
        active = False
    else:
        print(message)

while True:
    city = input("Enter you'r city")
    if city == "quit":
        break
    else:
        print(f'I"d love to go to {city.title()}')

num = 0
while num <10:
    num +=1
    if num %2 ==0:
        continue
    print(num)


#Упражнение 7.4
topping =[]
while True:
    add_toping=input("Pleasse enter topping to you'r pizza, or enter 'quit'")
    if add_toping !='quit':
        topping.append(add_toping)
    else:
        break
print(f"To you pizza added :")
for i in topping:
    print(f'\t{i}')


#Упражнение 7.5
while True:
    age = int(input("What is you'r age? : "))
    if age<3:
        print(f'You {age} years, ticket price is free')
    elif age <=12:
        print(f'You {age} years, ticket price is 10$')
    elif age >12:
        print(f'You {age} years, ticket price is 15$')


#Упражнение 7.6
active = True
while active:
    a=int(input('Enter any number: '))
    if a >= 60:
        print('You are old')
        break
    elif a<=0:
        print('you are not yet in this life')
        active = False
    elif 0<a<60:
        print('All good, rint next number!')
    else:
        break


#Упражнение 7.7
a=0
while a< 1:
    print(a)


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while "cat" in pets:
    pets.remove('cat')
print(pets)

responses ={}
polling_active = True
while polling_active:
    name = input('\nWhat is your name?')
    response = input('Which mountain would you like to climb someday?')
    responses[name] =response
    repeat = input('Would you like to let another person respond? (yes/ no)')
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
print(responses)
#Упражнение 7.8
sandwich_orders=['mana','bana','vama','faca']
finished_sandwiched = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made you {sandwich} sandwich!')
    finished_sandwiched.append(sandwich)
print(f'all sandwiches checked')
for finished in finished_sandwiched:
    print(finished)
#Упражнение 7.9
sandwich_orders=['mana','bana','vama','faca','pastrami','pastrami','pastrami']
finished_sandwiched = []
print(' We have not "pastrami"')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made you {sandwich} sandwich!')
    finished_sandwiched.append(sandwich)
print(f'all sandwiches checked')
for finished in finished_sandwiched:
    print(finished)
#Упражнение 7.10

invi = True
vacation={}
while invi:
    name = input('Enter you"r name: ')
    vaca = input('Enter where do you want to spend your vacation')
    vacation[name] = vaca
    question = input('Would you like to add a name "Yes / no"')
    if question == 'no':
        invi = False
        print('\n')
print('Who wants to go on vacation')
for key, value in vacation.items():
    print(f'{key.title()} wants to go on {value.title()}!' )
