import datetime
import calendar


current_datetime = datetime.date.today()

class Date:
    # Creates an object instance for the specified Gregorian date.
    def __init__(self, month=current_datetime.month, day=current_datetime.day, year=current_datetime.year):
        self._julianDay = 0
        self.year = year
        self.month = month
        self.day = day

        # The first line of the equation, T = (M - 14) / 12, has to be changed
        # since Python's implementation of integer division is not the same
        # as the mathematical definition.
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + \
            (1461 * (year + 4800 + tmp) // 4) + \
            (367 * (month - 2 - tmp * 12) // 12) - \
            (3 * ((year + 4900 + tmp) // 100) // 4)

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

    # The remaining methods are to be included at this point.

    def month_(self):
        greg_month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
    }
        for i in greg_month:
            if i == self.month:
                return greg_month[i]

    def numdays(self, other):
        day1 = self._julianDay
        day2 = other._julianDay

        return abs(day1 - day2)

    def shiftBy(self, shiftnumber):
        self._julianDay = self._julianDay + shiftnumber
        self._toGregorian()
        return self

    def dayOftheWeek(self):
        days_of_week = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"}
        x = self.dayOfWeek()
        for i in days_of_week:
            if i == x:
                return days_of_week[i]

    def _getDayYear(self):
        count = 0
        if self._isLeapYear():
            months_days = {
                "January": 31,
                "February": 29,
                "March": 31,
                "April": 30,
                "May": 31,
                "June": 30,
                "July": 31,
                "August": 31,
                "September": 30,
                "October": 31,
                "November": 30,
                "December": 31
            }
            month = self.month_()
            for i in months_days:
                if i != month:
                    count += months_days[i]
                    continue
                if i == month:
                    count += self.day
                    break
            return count


        elif not self._isLeapYear():
            months_days = {
                "January": 31,
                "February": 28,
                "March": 31,
                "April": 30,
                "May": 31,
                "June": 30,
                "July": 31,
                "August": 31,
                "September": 30,
                "October": 31,
                "November": 30,
                "December": 31
            }
            month = self.month_()
            for i in months_days:
                if i != month:
                    count += months_days[i]
                    continue
                if i == month:
                    count += self.day
                    break
                return count



    def calendar(self):
        print(list(calendar.day_abbr))

        return calendar.monthcalendar(self.year, self.month)

    def isWeekDay(self):
        x = self.dayOfWeek()
        days_of_week = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"}
        for x in days_of_week:
            if x != 5 or x != 6:
                return "Week day"
            else:
                return "Not a Week day"








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

    def _isValidGregorian(self, month, day, year):
        assert isinstance(month, int) and isinstance(day, int) and isinstance(year, int), "Inputs must be integers."
        if not (1 <= month <= 12):
            return False
        if year < 1:
            return False

        # Days per month, considering leap years for February
        days_in_month = [31, 29 if self._isLeapYear() == True else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return 1 <= day <= days_in_month[month - 1]

    # Determines if a given year is a leap year
    def _isLeapYear(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        else:
            return False