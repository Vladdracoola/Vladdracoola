class House:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.floor}')

    def __len__(self):
        return (self.floor)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(len(h1))
print(len(h2))
