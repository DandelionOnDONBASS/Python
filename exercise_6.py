alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print('\n')

new_points = alien_0['points']
print(f'You just earned {new_points} points!')
print('\n')

alien_0['x_position'] =0   #добавить  в словарь ключ х_position значение 0
alien_0['y_position'] =25  #добавить  в словарь ключ у_position значение 25
print(alien_0)
print('\n')

alien_0 ={}
alien_0['color'] = 'red'
alien_0['points'] = 10
print(alien_0)
print('\n')

alien_0['color'] = 'yellow'  #Изменение значения ключа color на yellow
print(alien_0)
print('\n')

alien_0 ={'x_position': 0, 'y_position':25, 'speed':'fast'}
print(f'Original position : {alien_0["x_position"]}')
# Пришелец перемещается вправо.
# Вычисляем величину смещения на основании текущей скорости.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed']=='medium':
    x_increment = 2
else:
    #Пришелец двигается быстро
    x_increment=3
# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print('\n')

alien_0 = {'color': 'green', 'points':5}
print(alien_0)
del alien_0['points']     #удаление значения в ключе point
print(alien_0)            # отменить удаление нельзя
print('\n')

favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward' : 'rubi',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sara'h favorite language is {language}")
print('\n')

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('point', 'No point value assigned')
print(point_value)
print('\n')

#Упражнение 6.1
man = {
    'first_name':'Ivan',
    'last_name': 'Ivanov',
    'age': 43,
    'city':'Kiev',
    }
print(man['age'])
print(man['city'])
print(man['first_name'])
print(man['last_name'])
print('\n')

#Упражнение 6.2
keys = {
    'ivan': 4,
    'oleg': 65,
    'kostia' : 44,
    'igor' : 47,
    }
print(f'Ivan favorite key {keys["ivan"]}')
print(f'Oleg favorite key {keys["oleg"]}')
print(f'Kostia favorite key {keys["kostia"]}')
print(f'Igor favorite key {keys["igor"]}')
print('\n')

#Упражнение 6.3
glossari= {
    "lower" : 'В нижнем регистре',
    'upper' : 'В верхнем регистре',
    'apped' : 'добавить в лист',
    'del': 'удалить значение',
    }
print(f'Lower : {glossari["lower"]} \nUpper : {glossari["upper"]} \nApped : {glossari["apped"]} \nDel : {glossari["del"]}\n')





user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items(): # выводим ключ и значение через перебор
    print(f'\nKey:{key}')
    print(f'VAlue: {value}')
print('\n')
    

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.") 
print('\n')

for name in favorite_languages.keys(): # вывод только ключей из словаря
    print(name.title())
print('\n')

favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward' : 'rubi',
    'phil': 'python',
    }

friends = ['phil', 'sarah']                 #Список друзей
for name in favorite_languages.keys():#Перебираем имена друзей из списка фаворит  лангуаже
    print(name.title())     #отобразить каждое имя
    if name in friends:         #перебор друзей из списка френдс
        language = favorite_languages[name].title()     #указываем язык по имени друга
        print(f"\t{name.title()}, I see you love {language}!") #показать сообщение с именем из списка френдс

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our pool')
print('\n')
for name in sorted(favorite_languages.keys()): #Сортировать только ключи в списке
    print(f'{name.title()}, thank you taking the pool')
print('\n')

for languages in favorite_languages.values():   #перебор только значений
    print(languages.title())
print('\n')

for languages in set(favorite_languages.values()): #выбор всех значений без повторений
    print(languages.title())
print('\n')

# Упражнение 6.4
glossari= {
    "lower" : 'В нижнем регистре',
    'upper' : 'В верхнем регистре',
    'apped' : 'добавить в лист',
    'del': 'удалить значение',
    'pYthon': 'key',
    'pythOn': 'value',
    'pythoN': 'image',
    'fdsdfs': 'fds',
    'dfsdf':'fds',
    }
for key, valuy in glossari.items():
    print(f'{key} {valuy}')
print('\n')
for key in set(glossari.keys()):
    print(key)
print('\n')
for value in set(glossari.values()):
    print(value)
print('\n')

rivers = {
    'dnepr':"ukraine",
    'nile':'egypt',
    'amazonka':'USA',
    'amure':'azia',
    }
for key, value in rivers.items():
    print(f'{key.title()} runs through {value.title()}.')
print('\n')
for key in rivers.keys():
    print(key.title())
print('\n')
for value in rivers.values():
    print(value.title())
print('\n')

# Упражнение 6.6
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward' : 'rubi',
    'phil': 'python',
    }
names = ['sarah','ivan','phil']
for name in names:
    if name in favorite_languages.keys():
        print(f'{name} прошел опрос')
    else:
        print(f'{name} не прошел опрос')
print('\n')



alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
alians = [alien_0,alien_1,alien_2]      #добавление всех словарей в список
for alian in alians:
    print(alian)
print('\n')


alians =[] #список из пришельцев куда будет добовлять их
for alian_num in range(30):    #создает 30 зеленых пришельцев
    new_alian = {'color': 'green','points': 5, 'speed': 'slow'}
    alians.append(new_alian)

for alien in alians[:5]:   #выводим первых 5 пришельцев
    print(alian)
print('...')

print(f'Total number of alians : {len(alians)}')
print('\n')

for alian in alians[0:3]:   #задаем в словари пришельцев знаяения
    if alian['color'] == 'green':
        alian['color'] = 'yellow'
        alian['speed'] = 'medium'
        alian['points'] = 10
for alian in alians[3:6]:
    if alian['color'] == 'green':
        alian['color'] = 'red'
        alian['speed'] = 'medium'
        alian['points'] = 10
for el in alians:
    print(el)
print('\n')

pizza = {
    'crust': 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
    }
print(f'You ordered a {pizza["crust"]} - crust pizza '
    "with the following toppings:")
for toping in pizza['toppings']:
    print(toping)
print('\n')
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell','c#'],
    }
for name, languages in favorite_languages.items():
    if len(languages)>=2:
        print(f"{name.title()}'s favorite languages are:")
        for language in languages:
            print(f'\t {language.title()}')
print('\n')

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',            #словарь в словаре
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f'\nUsername : {username}')
    fullname = f"{user_info['first']} {user_info['last']}"
    print(f"\tFull name : {fullname.title()}")
    print(f'\tLocation : {user_info["location"]}')
print('\n')
#Упражнение 6.7
Ivan = {
    'first_name':'Ivan',
    'last_name': 'Ivanov',
    'age': 43,
    'city':'Kiev',
    }
Kolia = {
    'first_name':'Kolia',
    'last_name': 'Koval',
    'age': 40,
    'city':'Kharkiv',
    }
Olia = {
    'first_name':'Olia',
    'last_name': 'Sudo',
    'age': 13,
    'city':'Lviv',
    }
people = [Ivan,Kolia,Olia]
for peple in people:
    fullname = f'{peple["first_name"]} {peple["last_name"]}'
    print(fullname)
    print(f'\tAge : {peple["age"]}')
    print(f'\tCity : {peple["city"]}')
print('\n')

#Упражнение 6.8
parrot= {
    'age': 4,
    'name':'kesha',
    'master':'ivan',
    'type':'parrot',
    }
cat= {
    'age': 2,
    'name':'kuzia',
    'master':'igor',
    'type':'cat',
    }  
dog= {
    'age': 6,
    'name':'vasia',
    'master':'sergey',
    'type':'dog',
    }  
pets = [parrot,cat,dog]
for pet in pets:
    print(f"{pet['master']}".title())
    print(f'\tPet age:{pet["age"]}')
    print(f'\tPet type: {pet["type"]}')
print('\n')
#Упражнение 6.9
print('\n')
favorite_places={
    'square': ['igor','sergey'],
    'lake' : ['ivan','igor','sergey'],
    'home': ['igor'],
    }
for key, value in favorite_places.items():
    print(f'In {key} like walk :')
    for val in value:
        print(f'\t {val.title()}')

#Упражнение 6.10
keys = {
    'ivan': [3,1,4,2,3,4],
    'oleg': [65,432,3543,453],
    'kostia' : [44,543,13,34,34,2,3],
    'igor' : [47,4534,532,45,3,45],
    }
for k,v in keys.items():
    print(f'Favorite nuvbers of {k.title()}')
    for val in v:
        print(f'\t{val}')

#Упражнение 6.11
cities = {
    'Kyev':{
        'country':'Ukraine',
        'population': 2400000,
        'fakt':'BEST CITY',
        },
    'Bad buhay':{
        'country':'Germany',
        'population': 400000,
        'fakt':'Myny farms',
        },
    'Paris':{
        'country':'France',
        'population': 2500000,
        'fakt':'Beautiful',
        },
    }
for city, value in cities.items():
    print(city)
    print(f'\t Country: {value["country"]}')
    print(f'\t Population :{value["population"]}')
    print(f'\t Fakt about thic citi: {value["fakt"]}')

#Упражнение 6.12
cities = {
    'Kyev':{
        'country':'Ukraine',
        'population': 2400000,
        'fakt':'BEST CITY',
        },
    'Bad buhay':{
        'country':'Germany',
        'population': 400000,
        'fakt':'Myny farms',
        },
    'Paris':{
        'country':'France',
        'population': 2500000,
        'fakt':'Beautiful',
        },
    }
for city, value in cities.items():
    print(city,value)
    if city =="Kyev":
        value['Presedent'] = 'Zelensky'
    elif city =="Bad buhay":
        value['Presedent'] = 'Frank-Walter Steinmeier'
    else:
        value['Presedent'] = 'Emmanuel Macron'
for city, value in cities.items():
    print(city)
    print(f'\t Country: {value["country"]}')
    print(f'\t Population :{value["population"]}')
    print(f'\t Fakt about thic citi: {value["fakt"]}')
    print(f'\t Presedent : {value["Presedent"]}')

