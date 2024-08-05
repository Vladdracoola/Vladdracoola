class Vehicle():
    __color_variants = ['red', 'black', 'white', 'yellow', 'blue']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f'Модель: {self.get_model()} \nМощность: {self.get_horsepower()} \nЦвет: {self.get_color()}'
              f' \nВладелец: {self.owner}')

    def set_color(self, new_color):
        new_color = str(new_color).lower()
        if new_color in self.__color_variants:
            self.__color = new_color
        else:
            print(f'Братик, ну какой {new_color}...')


class Sedan(Vehicle):
    __passenger_limit = 5

    def __init__(self, owner, __model, __engine_power, __color):
        super().__init__(owner, __model, __engine_power, __color)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
