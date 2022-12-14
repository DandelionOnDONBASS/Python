"""Класс для представления автомобиля"""
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

"""Классы для представления машин с бензиновым и электродвигателем."""

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        """Инициализация атрибутов аккумулятора."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()