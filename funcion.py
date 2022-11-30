def greet_user(username):
    """Выводит простое приветствие."""
    print(f"Hello!, {username.title()}! ")


greet_user('jesse')
greet_user('anton')
#Упражнение 8.1
def display_message(message):
    print(f'display a message {message.title()}')
display_message('this maseege')
#Упражнение 8.2
def favorite_book(title):
    print(f'One of my favorite book is {title.title()}')
favorite_book('Sherlock Holms')

def describe_pet(animal_type, pet_name):
    print(f'\nI have a {animal_type}.')
    print(f'My {animal_type}"s name is {pet_name.title()}')

describe_pet('hamster','harry')
describe_pet('dog','chichi')
describe_pet(animal_type='hamster', pet_name='harry')


def describe_pet(pet_name, animal_type='dog'):
    print(f'\nI have a {animal_type}.')
    print(f'My {animal_type}"s name is {pet_name.title()}')
describe_pet('willie')
describe_pet(pet_name='willie')

describe_pet('harry','hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
#Упражнение 8.3
def make_shirt(size,text):
    print(f'my shirt has this {size.title()} and this {text.title()}')
make_shirt('L','Big boss')
make_shirt('M','Little boss')

#Упражнение 8.4
def make_shirt(text = 'I like Python',size='L'):
    print(f'my shirt has this "{size.title()}" and this "{text.title()}"')
make_shirt()
make_shirt(size='M', text='MMMMM ssize')
#Упражнение 8.5
def describe_city(city_name, country_name):
    print(f'{city_name.title()} in in {country_name.title()}')
describe_city('Kyev', 'Ukraine')
describe_city('Nurnberg','Germany')
describe_city('paris','france')

def get_formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    full_name = f'{first_name} {middle_name} {last_name}'
    return full_name.title()
musician = get_formatted_name('jimi','lee', 'hendrix')
print(musician)
print('\n')

def get_formatted_name(first_name,last_name,Middle_name = ''):
    if Middle_name:
        full_name = f'{first_name} {Middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician= get_formatted_name('jimi','hooker','lee')
print(musician)

def build_person(first_name,last_name):
    person = {'first': first_name, 'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)

print('\n')
def build_person(first_name, last_name,age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('jimi','hendrix',23)
print(musician)

# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print('\nPlease tel me your name:')
#     f_name=input('First name: ')
#     if f_name=='':
#         print('input field is empty')
#         break
#     l_name = input('Last name:')
#     if l_name=='':
#         print('input field is empty')
#         break
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f'\nHello, {formatted_name}')


    #Упражнение 8.6
def city_country(city_name,country):
    full_name = f'{city_name},{country}'
    return full_name.title()
musician = city_country('paris','france')
print(musician)
musician = city_country('lviv','ukraine')
print(musician)
#Упражнение 8.7
def make_albom(frontman,albom_name):
    LP = {'Frontman': frontman, 'albom': albom_name}
    return LP
musician_1 = make_albom('Chester','Meteora')
print(musician_1)
musician_2 = make_albom('Mike','Hybrid Theory')
print(musician_2)
musician_3 = make_albom('Vova','One mory light')
print(musician_3)

print('\n')
#Упражнение 8.7_1
def make_albom(frontman,albom_name,tracs=''):
    LP = {'Frontman': frontman, 'albom': albom_name}
    if tracs:
        LP['tracs'] = tracs
    return LP
musician_1 = make_albom('Chester','Meteora')
print(musician_1)
musician_2 = make_albom('Mike','Hybrid Theory')
print(musician_2)
musician_3 = make_albom('Vova','One mory light',22)
print(musician_3)

# #Упражнение 8.8
# def make_albom(frontman,albom_name,tracs=''):
#     LP = {'Frontman': frontman, 'albom': albom_name}
#     if tracs:
#         LP['tracs'] = tracs
#     return LP
# while True:
#     print('please enter album name and artist')
#     F_m = input('Input frontman name:')
#     if F_m=='':
#         break
#     A_n = input('Input albom name: ')
#     if A_n == '':
#         break
#     FA=make_albom(F_m,A_n)
#     print(FA)

def greet_users(names):
    for name in names:
        print(f'Hello, {name.title()}')
username =['Ivan','roma','kolia']
greet_users(username)
print('\n')
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing model {current_design.title()}')
    completed_models.append(current_design.title())
print(f'\nThe following models have been printed:')
for complited_model in completed_models:
    print(complited_model)

    
print('\n')
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model : {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print(f'The following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
print('\n')
#Упражнение8.10
def show_messeges(meseges, send_masseges):
    while meseges:
        send_mas = meseges.pop()
        send_messages.append(send_mas)
def sen_messages(send_messages):
    print(f'Send messeges is : ')
    for send in send_messages:
        print(send)
msg = ['bahama mama','nintendo nintendo','vasilii terkin','ivanuski internation']
send_messages = []
show_messeges(msg, send_messages)
sen_messages(send_messages)
#Упражнение 8.11
def show_messeges(meseges, send_masseges):
    while meseges:
        send_mas = meseges.pop()
        send_messages.append(send_mas)
def sen_messages(send_messages):
    print(f'Send messeges is : ')
    for send in send_messages:
        print(send)
msg = ['bahama mama','nintendo nintendo','vasilii terkin','ivanuski internation']
send_messages = []
show_messeges(msg[:], send_messages)
sen_messages(send_messages)
print(msg)
print(send_messages)
print('\n')


def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra chesee')
print('\n')

def make_pizza(*toppings):
    print("\n Making a pizza with the following toppings:")
    for toping in toppings:
        print(f'\t-{toping}')
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra chesee')

def make_pizza(size,*toppings):
    print(f"\n Making a {size} pizza with the following toppings:")
    for toping in toppings:
        print(f'\t-{toping}')
make_pizza(16,'pepperoni')
make_pizza(24,'mushroom','green peppers','extra chesee')

def build_profile (first,last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert','enstein',
                            location = 'pricxetion',
                            field = 'physics')
print(user_profile)
print('\n')
#Упражнение 8.12

def burger_make(*burg):
    for k in burg:
        print(f'This burger is made up of: {k}')
        

burger_1 = ['bun', 'cutlet', 'tomato', 'cucmber']
burger_2 = ['bun', 'cutlet', 'tomato']
burger_make(burger_1,burger_2)
print('\n')
#Упражнение8.13
def build_profile(first, last,year, male, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['year'] = year
    user_info['male'] = male
    return user_info
user_profile = build_profile('albert', 'einstein',34,'man',
                            location='princeton',
                            field='physics')
for k,v in user_profile.items():
    print(f'{k} is {v}')
print('\n')
#Упражнение 8.14
def make_car(mark,back, **car_info):
    car_info['mark']= mark
    car_info['back'] = back
    return car_info
car = make_car('subaru','outback',color = 'blue', tow_package = True)
for k,v in car.items():
    print(f'{k} - {v}')







