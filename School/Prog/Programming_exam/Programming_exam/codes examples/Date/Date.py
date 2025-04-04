class Date:
    # Creates an object instance for the specified Gregorian date.
    def __init__(self, month, day, year):
        # Precondition: The provided date must be a valid Gregorian date.
        assert self._isValidGregorian(month, day, year), "Invalid Gregorian date."

        self._julianDay = 0

        # Adjusting the formula to account for Python's integer division
        tmp = -1 if month < 3 else 0

        self._julianDay = (day - 32075 +
                           (1461 * (year + 4800 + tmp) // 4) +
                           (367 * (month - 2 - tmp * 12) // 12) -
                           (3 * ((year + 4900 + tmp) // 100) // 4))

        # Postcondition: The Julian day number should be a positive integer.
        assert self._julianDay > 0, "Julian day calculation failed."

    # Extracts the appropriate Gregorian date component.
    def month(self):
        return self._toGregorian()[0]  # returning M from (M, d, y)

    def day(self):
        return self._toGregorian()[1]  # returning D from (m, D, y)

    def year(self):
        return self._toGregorian()[2]  # returning Y from (m, d, Y)

    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month += 12
            year -= 1
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

    def __add__(self, numOfDays):
        self._julianDay += numOfDays

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

    # Improved validation function for Gregorian dates
    def _isValidGregorian(self, month, day, year):
        assert isinstance(month, int) and isinstance(day, int) and isinstance(year, int), "Inputs must be integers."
        if not (1 <= month <= 12):
            return False
        if year < 1:
            return False

        # Days per month, considering leap years for February
        days_in_month = [31, 29 if self._isLeapYear(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return 1 <= day <= days_in_month[month - 1]

    # Determines if a given year is a leap year
    def _isLeapYear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
