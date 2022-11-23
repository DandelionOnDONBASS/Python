players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
a=[]
for player in players[:3]:
    print(player.title())
    a.append(player)
print(a)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are : ")
print(friend_foods)
print('\n')


#Упражнение 4.10
fruts = ['apple','potata','kivi','orange']
print('The irst three items in the list are:', fruts[:3])
print('Three items from the middle of the list are:',fruts[1:3])
print('The last three items in the list are:',fruts[-3:],'\n')

#Упражнение 4.11

my_pizza = ['Ananases','Carbonara','Pepperoni','Carlione','Mafia']
friend_pizzas = my_pizza[:]
friend_pizzas.append('Carbonos')
print('My favorite pizzas are:')
for my_piz in my_pizza:
    print(my_piz)
print('\n')

print('My friends favorite pizza are:')
for fr_piz in friend_pizzas:
    print(fr_piz)
print('\n')

#Упражнение 4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
for mf in my_foods:
    print(mf)
print('\n')
for ff in friend_food:
    print(ff)



