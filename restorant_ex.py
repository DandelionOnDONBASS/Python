


class User():
    def __init__(self,first_name,second_name,last_name, user_age):
        self.name = first_name
        self.ln = last_name
        self.sn = second_name
        self.age = user_age
        self.login_attempts = 0
    def describe_user(self):
        print(f'My name is {self.name}')
        print(f'My last name is {self.ln}')
        print(f'My age is {self.age}')
    def greet_user(self):
        print(f'Hello {self.name} {self.ln} {self.sn}')
    def increment_login_attemts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts = 0

# user_1 = User('Anna','Petrova','Victorovna',23)
# user_1.greet_user()
# user_1.increment_login_attemts()
# user_1.increment_login_attemts()
# user_1.increment_login_attemts()
# print(user_1.login_attempts)
# user_1.reset_login_attempts()
# print(user_1.login_attempts)


class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_testorant(self):
        print(f'Restaurant name is {self.name}')
        print(f'Kitchen is {self.type}')
    def open_restaurant(self):
        print(f'Restaurant {self.name} is open')
    def num_served(self):
        print(f'This retarant are {self.number_served}')
    def set_restarant_served(self,num):
        if num >= self.number_served:
            self.number_served = num
        else:
            print('NOT')
    def increment_num_served(self,num):
        self.number_served+=num
    

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['shok','banana']
    def IceCreamStand(self):
        for i in self.flavors:
            print(i)
class Privilages():
    def __init__(self,privilages_admin =["разрешено удалять пользователей", "разрешено банить пользователей"]):
        self.privilages = privilages_admin
    def show_privilages(self):
        print('\tAdmin privilages:')
        for i in self.privilages:
            print(i)
            
class Admin(User):
    def __init__(self, first_name, second_name, last_name, user_age):
        super().__init__(first_name, second_name, last_name, user_age)
        """атрибут для привелегий админа"""
        self.privilages = Privilages()
        self.privilages_admin = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]
    def show_privilages(self):
        print('\tAdmin privilages:')
        for i in self.privilages_admin:
            print(i)

# ttt=IceCreamStand('Chacha','Ice')
# ttt.IceCreamStand()
# Admin_Ivan = Admin('Ivan','Petrovich','Kylic',32)
# Admin_Ivan.describe_user()
# Admin_Ivan.show_privilages()
# Admin_Ivan.privilages.show_privilages()

