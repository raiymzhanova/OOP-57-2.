# инкапсуляция
class UserAccount:

    def __init__(self, username, password):
        self.username = username
        self._balance = 0
        self.__password = password
        self._is_logged_in = False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Баланс пополнен на {amount}. Текущий баланс: {self._balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):

        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Со счёта списано {amount}. Текущий баланс: {self._balance}")
            else:
                print("Ошибка: недостаточно средств.")
        else:
            print("Сумма списания должна быть положительной.")

    def login(self, password):
        if self.__password == password:
            self._is_logged_in = True
            print("Доступ разрешён.")
        else:
            print("Доступ запрещён: неверный пароль.")
            self._is_logged_in = False

    def get_balance(self):
        if self._is_logged_in:
            return self._balance
        else:
            return "Ошибка: доступ запрещён. Сначала войдите в аккаунт."

# Пример использования
my_account = UserAccount("john_doe", "supersecret123")

my_account.login("wrong_password")
print(my_account.get_balance())

my_account.login("supersecret123")
print(my_account.get_balance())

my_account.deposit(500)
my_account.withdraw(100)
my_account.withdraw(600)



# Абстракция
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Transport):

    def move(self):
        return "Машина едет по дороге."

    def fuel_type(self):
        return "Топливо: бензин."


class Bike(Transport):
    def move(self):
        return "Велосипед едет по дороге."

    def fuel_type(self):
        return "Топливо: мускульная сила."


class Plane(Transport):

    def move(self):
        return "Самолёт летит."

    def fuel_type(self):
        return "Топливо: керосин."

# Пример использования

car = Car()
bike = Bike()
plane = Plane()

print(car.move())
print(car.fuel_type())
print(bike.move())
print(bike.fuel_type())
print(plane.move())
print(plane.fuel_type())