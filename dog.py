class Dog():        #Определяется класс Dog
    """Простая модель собаки"""

    def __init__(self,name,age):#__init__ метод(специальный метод)(self,name, age - параметры)(__init__ для создания экземпляра Dog)
        """Инициализирует аррибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собка садится по команде"""
        print(f'{self.name} is now sittisng')

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f'{self.name} rolled over!')

my_dog=Dog('Willie',6)
print(f'My dog"s name is {my_dog.name}.')
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()
print('\n')

your_dog = Dog('Lusie',4)
print(f'My dog"s name is {my_dog.name}')
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
print('\n')

print(f'You"r dog is {your_dog.name}')
print(f'You"r dor is {your_dog.age} years old.')
your_dog.sit()
print('\n')


