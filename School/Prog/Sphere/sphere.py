from math import pi

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def surface(self):
        return 4 * pi * (self.radius**2)


    def volume(self):
        return 4/3 * pi * self.radius**3

    def __repr__(self):
        return  f"radius is {self.radius}, area is {self.surface()}, volume is {self.volume()}"