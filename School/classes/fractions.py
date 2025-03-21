

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def sum_of_vals(self):
        if s1.denominator > s2.denominator:
            return f"{(s2.numerator * s1.denominator)+s1.numerator}/{s1.denominator}"
        elif s2.denominator > s1.denominator:
            return f"{(s1.numerator * s2.denominator)+s2.numerator}/{s2.denominator}"
        elif s2.denominator == s1.denominator:
            return f"{s1.numerator + s2.numerator}/{s1.denominator}"

    def product(self):
        return f"{s1.numerator * s2.numerator}/{s1.denominator * s2.denominator}"

    def opposite(self):
        oppositenum = self.numerator * -1
        oppositedenom = self.denominator
        return  f"{oppositenum}/{oppositedenom}"

    def invert(self):
        temp_holder = self.denominator
        denominator = self.numerator
        numerator = temp_holder
        new_frac = f"{numerator} / {denominator}"
        return new_frac


    def __repr__(self):
        return  f"sum is {self.sum_of_vals()}, product is {self.product()}, opposite is {self.opposite()},inversion is {self.invert()}"


def GCD(a,b):
    if b == 0:
        return a
    else:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r
            GCD(a,b)

if __name__ == "__main__":

    s1 = Fraction(7 , 4)
    s2 = Fraction(8, 2)

    print(f"{s1}\n,{s2}")

    GCD(s1.denominator, s2.denominator)


    print(f"{s1}\n,{s2}")
