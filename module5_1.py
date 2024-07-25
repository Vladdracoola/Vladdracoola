class House:
    def __init__(self, name, floor, new_floor):
        self.name = name
        self.floor = floor
        self.go_to(new_floor)

    def go_to(self, new_floor):
        if new_floor > self.floor or new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Горский', 18, 5)
h2 = House('Домик в деревне', 2, 10)
