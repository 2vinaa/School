# Extracts a collection of birth dates from the user and determines # if each individual is at least 21 years of age.
from date import Date


def assignment_1():
    # ASSIGNMENT 1
    print("********************************************************************")
    print("* ASSIGNMENT 1                                                     *")
    print("********************************************************************")

    # 1.1 monthName
    today = Date(2, 22, 2022)
    print(f"Month name for: {today.asGregorian()}")
    print(today.monthName())
    print()

    # 1.2 isLeapYear
    today = Date(2, 22, 2022)
    print(f"Is leap year for: {today.asGregorian()}")
    print(today.isLeapYear())
    today = Date(2, 22, 2021)
    print(f"Is leap year for: {today.asGregorian()}")
    print(today.isLeapYear())
    print()

    # 1.3 numDays
    today = Date(1, 31, 2021)
    other_day = Date(1, 1, 2021)
    print(f"Days from {other_day.asGregorian()} to {today.asGregorian()}")
    print(today.numDays(other_day))
    print()

    # 1.4 advanceBy
    today = Date(1, 31, 2021)
    print(f"Advance by 1 from: {today.asGregorian()}")
    today.advanceBy(1)
    print(today.asGregorian())
    print()

    # 1.5 isValidGregorian
    valid = True
    try:
        today = Date(1, 31, 2021)
    except AssertionError:
        valid = False
    print(f"Is valid Gregorian date: 1/31/2021: {valid}")

    valid = True
    try:
        Date(1, 32, 2021)
    except AssertionError:
        valid = False
    print(f"Is valid Gregorian date: 1/32/2021: {valid}")
    print()


def assignment_2():
    # ASSIGNMENT 2
    print("********************************************************************")
    print("* ASSIGNMENT 2                                                     *")
    print("********************************************************************")

    # 2.1 dayOfTheWeekName
    today = Date(2, 1, 2021)
    print(f"Day of the week name for: {today.asGregorian()}")
    print(today.dayOfTheWeekName())
    print()

    # 2.2 dayOfTheYear
    today = Date(2, 1, 2021)
    print(f"Day of the year for: {today.asGregorian()}")
    print(today.dayOfYear())
    print()

    #  2.3 isWeekday
    today = Date(1, 31, 2021)
    print(f"Is week day for: {today.asGregorian()}")
    print(today.isWeekday())
    today = Date(1, 29, 2021)
    print(f"Is week day for: {today.asGregorian()}")
    print(today.isWeekday())
    print()

    # 2.4 isEquinox
    today = Date(9, 22, 2021)
    print(f"Is equinox for: {today.asGregorian()}")
    print(today.isEquinox())
    today = Date(9, 1, 2021)
    print(f"Is equinox for: {today.asGregorian()}")
    print(today.isEquinox())
    print()

    # 2.5 isSolstice
    today = Date(12, 21, 2021)
    print(f"Is solstice for: {today.asGregorian()}")
    print(today.isSolstice())
    today = Date(9, 1, 2021)
    print(f"Is solstice for: {today.asGregorian()}")
    print(today.isSolstice())
    print()

    # 2.6 asGregorian
    today = Date(12, 21, 2021)
    print(f"As Gregorian: {today.asGregorian()}")
    print(today.asGregorian())
    print(today.asGregorian("."))
    print()


def printCalendar(date: Date):
    current_month = date.month()
    first_day_of_month = Date(current_month, 1, date.year())
    day_of_the_week = first_day_of_month.dayOfWeek()

    curr_day_of_the_week = 6  # sunday

    elements = []

    # fill padding elements
    while curr_day_of_the_week != day_of_the_week:
        elements.append(" ")
        curr_day_of_the_week = (curr_day_of_the_week + 1) % 7

    # fill dates
    while first_day_of_month.month() == current_month:
        elements.append(first_day_of_month.day())
        first_day_of_month.advanceBy(1)

    # print the data
    print(f"\t  {date.monthName()} {date.year()}")
    print("Su\tMo\tTu\tWe\tTh\tFr\tSa")

    for i, e in enumerate(elements):
        print(f"{e}\t", end="")
        if i % 7 == 6:
            print()
    print()
    print()


# Call the main routine.
if __name__ == '__main__':
    assignment_1()
    assignment_2()

    # ASSIGNMENT 3
    today = Date(1, 31, 2021)
    printCalendar(today)

    # ASSIGNMENT 4
    today = Date(year=2001)
    print(f"Date using year 2001 ony {today.asGregorian()}")


