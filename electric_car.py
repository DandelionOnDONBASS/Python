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

class Battery():
    """Простая моель аккумулятора электромобиля"""
    def __init__(self,battery_size = 75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f'Thus car has a {self.battery_size}-kWh battery.')
    def upgrade_battery(self):
        if self.battery_size<= 100:
            self.battery_size =100

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size ==75:
            range =260
        elif self.battery_size == 100:
            range = 315
        print(f'This car can go about {range} miles on a full charge')
class ElectricCar(Car):
    """Представляет спектр машины, спецефически для электромобилей"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, спецефические для электромобиля"""
        super().__init__(make,model,year)
        self.battery = Battery()
        self.battery_size = 75
    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print('This car doesn"t need a gas tank!')
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

        
my_tesla = ElectricCar('teslf','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()


teslf= ElectricCar('tesla','aser','2012')
teslf.battery.get_range()
teslf.battery.upgrade_battery()
teslf.battery.get_range()
