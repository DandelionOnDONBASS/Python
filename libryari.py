from random import randint
from random import choice
# a=[4,3,6,54,4,324,5,45,32,45,3,]
# print(choice(a))    #Рандомное значение из списка "а"

# print(randint(1,9))  #Рандомное значение от 1 до 9

class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))

# koub = Die()
# koub_2 = Die(10)
# koub_3 = Die(20)
        # class Lott():
#     def __init__(self,lot = loterrea):
#         self.lot = lot
#     def win_tick(self):       
#         win = choice(self.lot),choice(self.lot)
#         print(win)

        
    
       

# tick_1 = Lott()
# tick_1.win_tick()

loterrea = [1,2,3,4,5,6,7,8,9,0]
my_win_tick = (2,1,7,7)
win = choice(loterrea),choice(loterrea),choice(loterrea),choice(loterrea)
#print(win)
tickets=[]
k=1
while my_win_tick != (choice(loterrea),choice(loterrea),choice(loterrea),choice(loterrea)):
    win=(choice(loterrea),choice(loterrea),choice(loterrea),choice(loterrea))
    #print(win)
    tickets.append(win)
    k+=1
print(tickets)
print(k)




