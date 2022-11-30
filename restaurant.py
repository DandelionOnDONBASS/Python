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
restaurant = Restaurant('Mazzera','Italiano')
restaurant_u=Restaurant('Hohol','Ukrainian')
restaurant_f=Restaurant('Ulala','France')
restaurant_u.describe_testorant()
restaurant_f.describe_testorant()
print(f'New restaurant {restaurant.name} with {restaurant.type} kitchen')
restaurant.describe_testorant()
restaurant.open_restaurant()

restaurant_k=Restaurant('Moldova','Moldovanian')
restaurant_k.number_served = 23


class User():
    def __init__(self,first_name,second_name,last_name, user_age):
        self.name = first_name
        self.ln = last_name
        self.sn = second_name
        self.age = user_age
    def describe_user(self):
        print(f'My name is {self.name}')
        print(f'My last name is {self.ln}')
        print(f'My age is {self.age}')
    def greet_user(self):
        print(f'Hello {self.name} {self.ln} {self.sn}')
user_1 = User('Ivan','Ivanovich','Petrov',34)
user_2 = User('Igor','Sergeevich','Koba',43)
user_1.greet_user()
user_1.describe_user()
user_2.greet_user()
user_2.describe_user()

