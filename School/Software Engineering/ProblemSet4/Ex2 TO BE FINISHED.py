from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make:str, model:str, year:int, daily_r:float):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__daily_rate = daily_r

    @abstractmethod
    def calculate_rental_costs(self,days: int):
        return self.__daily_rate * days

class Car(Vehicle):
    def __init__(self, make:str, model:str, year:int, daily_r:float, seats : int):
        Vehicle.__init__(self, make, model, year, daily_r)
        self.seats = seats

    def calculate_rental_costs(self,days: int):
        return Vehicle.calculate_rental_costs(self, days)