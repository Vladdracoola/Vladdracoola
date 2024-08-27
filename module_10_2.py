import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power, enemy_power=100):
        super().__init__()
        self.name = str(name)
        self.power = int(power)
        self.enemy_power = enemy_power

    def run(self):
        days = 0
        print(f'{self.name}, На нас напали!')
        while self.enemy_power > 0:
            days += 1
            self.enemy_power -= self.power
            print(f'{self.name}, сражается {days} дней, осталось противников: {self.enemy_power}' + '\n')
            time.sleep(1)
        print(f'{self.name}, одержал победу спустя {days} дней! За Oрду!!!' + '\n')


first_knight = Knight('Sir Durotan', 10)
second_knight = Knight("Sir Thrall", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились победой Орды!')
