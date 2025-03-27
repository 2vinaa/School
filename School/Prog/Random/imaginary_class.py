
class Image:
    def __init__(self, imaginary, real):
        self.real = real
        self.imaginary = imaginary

    def som(self, c2):
        r = self.real + c2.real
        i = self.imaginary + c2.imaginary
        return Image(r, i)

    def subtr(self, c2):
        r = self.real - c2.real
        i = self.imaginary - c2.imaginary
        return Image(r, i)

    def mult(self, c2):
        r = self.real * c2.real
        i = self.imaginary * c2.imaginary
        return Image(r, i)

    def dis(self):
        r = self.real
        i = self.imaginary
        return Image(r, i)


    def __repr__(self):
        return  f"{self.real} + {self.imaginary}i"



