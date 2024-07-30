class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.floor}')

    def __len__(self):
        return (self.floor)

    def __del__(self):
        print (f'"{self.name}" снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3


print(House.houses_history)