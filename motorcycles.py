motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle= motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f'The last motorcycle I owned was a {popped_motorcycle.title()}')
first_owner = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owner.title()}')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#УПРАЖНЕНИЕ 3.4
guests = ['masha','ivan','jenia']
print(f'Hello, {guests[0].title()} ,I want to invite you to my birthday!')
print(f'Hello, {guests[1].title()} ,I want to invite you to my birthday!')
print(f'Hello, {guests[2].title()} ,I want to invite you to my birthday!')
#упражнение 3.5
guests_not=guests.pop(1)
print(guests_not)
print(guests)
guests.append('Gena')
print(guests)
print(f'Hello, {guests[0].title()} ,I want to invite you to my birthday!')
print(f'Hello, {guests[1].title()} ,I want to invite you to my birthday!')
print(f'Hello, {guests[2].title()} ,I want to invite you to my birthday!')

#Упражнение 3.6
print("\n There will be more guests")
guests.insert(0, 'Kostia')
guests.append('Alina')
print(guests)
print(f'Hello, {guests[0].title()} ,I want to invite you to my birthday!')
print(f'Hello, {guests[1].title()} ,I want to invite you to my birthday!')
print(f'Hello, {guests[2].title()} ,I want to invite you to my birthday!')
print(f'Hello, {guests[3].title()} ,I want to invite you to my birthday!')
print(f'Hello, {guests[4].title()} ,I want to invite you to my birthday!')

#Упражнение 3.7
print(guests)
print('sorry, only two are invited to dinner')
no_guest_1 = guests.pop(0)
print(f'sorry {no_guest_1} but without you')
no_guest_2 = guests.pop(0)
print(f'sorry {no_guest_2} but without you')
no_guest_3= guests.pop(0)
print(f'sorry {no_guest_3} but without you')

print(guests)
print(f'Hello {guests[0]} , Offer valid')
print(f'Hello {guests[1]} ,Offer valid')
del guests[0]
del guests[0]

print(guests)