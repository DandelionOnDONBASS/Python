requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!\n")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f'adding {requested_topping}')
print('\nFinished making your pizza\n')



requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print('\n')
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print('\nFinished making your pizza!')


#Упражнение 5.8
name_user=['admin','ivan','stepan','igor','sergii']
for name in name_user:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for logging in again')

#Упражнение 5.9
name_user=['admin','ivan','stepan','igor','sergii']
if name_user:
    for name in name_user:
        print('Users YES')
        break
else:
    print('Users NOT')
print('\n')

name_user=[]
if name_user:
    for name in name_user:
        print('Users YES')
        break
else:
    print('Users NOT/n')


#Упражнение 5.10
current_users=['kaTia','IVan','stEpan','igOr','sergii','vasia']
current_users = [x.lower() for x in current_users]
new_users=['vOva','jEnia','iVan','stEpan','Oleg']
new_users = [x.lower() for x in new_users]
for new_user in new_users:
    if new_user in current_users:
        print(f'Please,{new_user.title()} great new name')
    else:
        print(f'All good,{new_user.title()} come in')
print('\n')

#Упражнение 5.11
for i in range(1,10):
    if i ==1:
        print(f'{i}st')
    if i ==2:
        print(f'{i}nd')
    if i==3:
        print(f'{i}rd')
    if i >=3:
        print(f'{i}th')

