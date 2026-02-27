
class Date:
    Days31 = [1, 3, 5, 7, 8, 10, 12]
    Days30 = [4, 6, 9, 11]

    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__isLeapYear = False

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if 1930 <= value <= 2130:
            self.__year = value
        else:
            pass


    @property
    def month(self):
        return self.__month


    @month.setter
    def month(self, value):
        if 1 <= value <= 12:
            self.__month = value
        else:
            pass


    @property
    def day(self):
        return self.__day


    @day.setter
    def day(self, value):
        if 1 <= value <= 31:
            self.__day = value


    def check_for_leap_year(self):
        if (self.__year % 4 == 0 and self.__year % 100 != 0) or (self.__year % 400 == 0):
            self.__isLeapYear = True
            return f"{self.__year} is {self.__isLeapYear}"


    def check_valid_date(self):
        if self.__month in Days31:
            if 1 <= self.__day <= 31:
                return "The given date is valid"
            else:
                return "The given date is invalid"

        elif self.__month in Days30:
            if 1 <= self.__day <= 30:
                return "The given date is valid"
            else:
                return "The given date is invalid"

        else:
            if self.__isLeapYear is True:
                if self.__month == 2:
                    if 1 <= self.__day <= 29:
                        return "The given date is valid"
                    else:
                        return "The given date is invalid"
            else:
                if self.__month == 2:
                    if 1 <= self.__day <= 28:
                        return "The given date is valid"
                    else:
                        return "The given date is invalid"
