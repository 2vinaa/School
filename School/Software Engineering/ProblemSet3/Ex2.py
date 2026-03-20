class BankingAccount:
    def __init__(self, id:int, first_name:str, last_name:str):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = 0

    def withdraw(self, value:float):
        if value > 0:
            self.__balance -= value
            return self.__balance
        else:
            return "Cant withdraw negative numbers"

    def deposit(self, value):
        if value > 0:
            self.__balance += value
            return self.__balance

class SavingAccount(BankingAccount):
    def __init__(self, first_name:str, last_name:str):
        super().__init__(first_name, last_name)
        self.__balance = 50

    def withdraw(self, value:float):
        if value <= 10000:
            self.__balance -=5
            super().withdraw(value)