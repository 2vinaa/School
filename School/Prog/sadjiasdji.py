class Date:
    def __init__ (self, day, month, year):
        self.day=day
        self.month=month
        self.year=year


    def __lt__(self, other):
     return (self.year,
    self.month, self.day) < (other.year,
    other.month, other.day)


if __name__ == "__main__":
    d1 = Date(10, 5, 2024)
    d2 = Date(11, 5, 2024)


    print(d1 < d2)