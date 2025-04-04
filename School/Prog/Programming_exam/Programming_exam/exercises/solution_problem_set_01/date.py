from datetime import date


class Date:

    # ASSIGNMENT 3
    def __init__(self, month=None, day=None, year=None):
        today = date.today()
        if month is None:
            month = today.month
        if day is None:
            day = today.day
        if year is None:
            year = today.year

        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), "Invalid Gregorian date."
        tmp = 0
        if month < 3:
            tmp = -1
        # the Julian day is how many days have elapsed since 1st of Jan, 4713 BC
        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + \
                          (367 * (month - 2 - tmp * 12) // 12) - \
                          (3 * ((year + 4900 + tmp) // 100) // 4)
        self._month_names = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        self._week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    # Extracts the appropriate Gregorian date component.
    def month(self):
        return (self._toGregorian())[0]  # returning M from (M, d, y)

    def day(self):
        return (self._toGregorian())[1]  # returning D from (m, D, y)

    def year(self):
        return (self._toGregorian())[2]  # returning Y from (m, d, Y)

    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400) % 7

    # Returns the date as a string in Gregorian format.
    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)

    # Logically compares the two dates.
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    # Returns the Gregorian date as a tuple: (month, day, year).
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    #   The remaining methods are to be included at this point.
    # ......

    # ASSIGNMENT 1

    # 1.1)
    def monthName(self):
        return self._month_names[self.month() - 1]

    # 1.2)
    def isLeapYear(self, year=None):
        if year is None:
            year = self.year()
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        return False

    # 1.3)
    def numDays(self, otherDate):
        return abs(self._julianDay - otherDate._julianDay)

    # 1.4)
    def advanceBy(self, days):
        assert self._julianDay - days > 0, "Dates cannot be less than November 24, 4714 BC"

        self._julianDay += days

    # 1.5)
    def _isValidGregorian(self, month, day, year):
        # outside the valid range
        if 1 > month > 12 or 1 > day > 31 or year < -4713:
            return False

        # months with only 30 days
        if month in [4, 6, 9, 11] and day > 30:
            return False

        # february is a special case
        if month == 2:
            if self.isLeapYear(year) and day > 29:
                return False
            elif day > 28:
                return False

        # if no filter returned, it is a valid date
        return True

    # ASSIGNMENT 1

    # 2.1)
    def dayOfTheWeekName(self):
        return self._week_days[self.dayOfWeek()]

    # 2.2)
    def dayOfYear(self):
        current_year = self.year()
        first_day_year = Date(1, 1, current_year)
        return self.numDays(first_day_year) + 1

    # 2.3
    def isWeekday(self):
        return self.dayOfWeek() in range(5)

    # 2.4
    def isEquinox(self):
        current_year = self.year()
        equinoxes = (Date(3, 20, current_year), Date(9, 22, current_year))
        return self in equinoxes

    # 2.5
    def isSolstice(self):
        current_year = self.year()
        equinoxes = (Date(6, 21, current_year), Date(12, 21, current_year))
        return self in equinoxes

    # 2.6
    def asGregorian(self, divchar='/'):
        return f"{self.month()}{divchar}{self.day()}{divchar}{self.year()}"
