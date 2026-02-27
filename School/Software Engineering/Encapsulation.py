import random

class SimCard:

    MAX_ATTEMPTS = 3

    def __init__(self, telephone_number:int, firstname:str, lastname:str, pin: str):
        self.__number = telephone_number
        self.__name = firstname
        self.__surname = lastname
        self.__pin = pin
        self.__attempts = SimCard.MAX_ATTEMPTS
        self.__isLocked = True

    def reset_attempts(self):
        self.__attempts = 3

    def call_assistance(self):
        if self.__attempts == 0:
            time.sleep(86400)
            return self.reset_attempts()
        else:
            return "You still have attempts"


    def unlock(self,code):
        if self.__isLocked:
            if self.__attempts != 0:
                if self.__pin == code:
                    self.__isLocked = False
                    self.reset_attempts()
                else:
                    self.__attempts -= 1
                    return f"Wrong Code, {self.__attempts} Attempts Remaining"

            else:
                self.callassistance()


    @property
    def name(self):
        if self.__isLocked is False:
            return self.__name
        else:
            pass

    @name.setter
    def name(self,name:str):
        if self.__isLocked is False:
            self.__name = name
        else:
            pass

    @property
    def lastname(self):
        if self.__isLocked is False:
            return self.__surname
        else:
            pass

    @lastname.setter
    def lastname(self, lastname:str):
        if self.__isLocked is False:
            self.__surname = lastname
        else:
            pass

    @property
    def phone_number(self):
        if self.__isLocked is False:
            return self.__number
        else:
            pass

    @phone_number.setter
    def phone_number(self, phone_number:int):
        if self.__isLocked is False:
            self.__number = phone_number
        else:
            pass



if __name__ == "__main__":
    s1 = SimCard(3420470205, "Federico", "Lombardo", "9191")
    print(s1.unlock("91829"))
    s1.unlock("9191")
    print(s1.phone_number)
    s1.phone_number = 2929
    print(s1.phone_number)
