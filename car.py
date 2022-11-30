class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):  #Вызывать метод через print()
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Выводит пробег машины в милях"""
        print(f'This car has {self.odometer_reading} miles on it.')
    def update_odometer (self, mileage):
        """Устанавливает заданое значение на одометр
        При попытке обратной подкрутки изменение отклоняется"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f'You can not roll back an odometer')
    def increment_odometer(self,miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading+=miles


my_user_car = Car('subaru','outback','2015')
print(my_user_car.get_descriptive_name())
my_user_car.update_odometer(23_500)
my_user_car.read_odometer()
my_user_car.increment_odometer(100)
my_user_car.read_odometer()


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# # my_new_car.odometer_reading = 23   #Изменение одометра - первый способ
# # my_new_car.read_odometer()
# my_new_car.update_odometer(55) #Изменение одометра - второй способ
# my_new_car.read_odometer()