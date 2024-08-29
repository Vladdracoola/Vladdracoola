from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.q = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'"{guest.name} сел(-а) за стол номер {table.number}".')
                    break
            else:
                print(f'"{guest.name} в очереди"')
                self.q.put(guest)

    def discuss_guests(self):
        while not self.q.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f' "{table.guest.name} покушал(-а) и ушёл(ушла)"')
                    print(f'"Стол номер {table.number} свободен"')
                    table.guest = None
                if table.guest is None and not self.q.empty():
                    guest = self.q.get()
                    table.guest = guest
                    guest.start()
                    print(f'"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
