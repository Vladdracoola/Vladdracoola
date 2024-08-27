import time
import threading
from threading import Lock
import random


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for transaction in range(100):
            increase = random.randint(50, 500)
            self.balance += increase
            print(f'Пополнение {increase}. Баланс: {self.balance}' + '\n')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for transaction in range(100):
            decrease = random.randint(50, 500)
            print(f'Запрос на снятие {decrease}' + '\n')
            if decrease <= self.balance:
                self.balance -= decrease
                print(f'Снятие {decrease}. Баланс: {self.balance}' + '\n')
            else:
                print(f'Запрос отклонён. Недостаточно средств' + '\n')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank(0)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
