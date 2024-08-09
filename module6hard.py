import math


class Figure():
    sides_count = 0
    filled = False
    def __init__(self, __color, __sides):
        if not isinstance(__sides, list):
            __sides = [__sides]
        if len(__sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = __sides
        self.__color = __color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for color in (r, g, b):
            if not isinstance(color, int) or not (0 <= color <= 255):
                return False
        return True

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int) and side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.radius = self.get_sides()[0]

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        return  self.radius / 2 * 3.14


class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.height = self.calculate_height()

    def get_square(self):
        a, b, c = self.get_sides()
        p = self.__len__() / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return S

    def calculate_height(self):
        a, b, c = self.get_sides()
        S = self.get_square()
        height = (2 * S) / a
        return height


class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, __sides):
        super().__init__(__color, [__sides] * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 35, 100), 5)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 22, 44)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Всё о треугольниках
triangle1.set_color(55, 66, 77)
print(triangle1.get_color())
triangle1.set_sides(22,22)
print(triangle1.get_sides())
print(triangle1.get_square())
print(triangle1.calculate_height())
