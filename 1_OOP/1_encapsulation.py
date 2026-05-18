'''
    Первый вариант
'''

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return 'Not enough money'

    def get_balance(self):
        return self.__balance


'''
    Второй вариант
'''

class BankAccount2:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return 'Not enough money'