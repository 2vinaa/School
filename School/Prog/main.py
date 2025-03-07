# Test main function

from abstractiontest import Date

if __name__ == "__main__":
    dates = [
        Date(2, 29, 2024),  # Leap year
        Date(12, 31, 1999),  # End of the century
        Date(1, 1, 2000),  # Beginning of the millennium
        Date(6, 15, 2023)  # Random date
    ]

    datemm = Date(year=2001)
    print(datemm)

    for date in dates:
        print(f"Date: {date}, Day of week: {date.dayOfWeek()}")

    # Comparison test
    print("Comparison Test:")
    assert dates[0] > dates[1], "Comparison failed: Expected True"
    assert dates[2] != dates[3], "Comparison failed: Expected True"
    print(f"{dates[0]} < {dates[1]}: {dates[0] < dates[1]}")
    print(f"{dates[2]} == {dates[3]}: {dates[2] == dates[3]}")

    print(dates[0])


    print(dates[0].month_())

    print(dates[0]._isLeapYear())
    print(dates[0]._julianDay)
    print(dates[0].calendar())