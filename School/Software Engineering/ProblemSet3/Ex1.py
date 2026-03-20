import numpy as np

class Circle:
    def __init__(self, radius:float, color:str):
        self.__rad = radius
        self.__color = color

    @property
    def radius(self):
        return self.__rad

    @radius.setter
    def radius(self, value):
        self.__rad = value

    @property
    def colour(self):
        return self.__color

    @colour.setter
    def colour(self, value):
        self.__color = value

    def circumference(self):
        return self.__rad * np.pi * 2


    def surface_area(self):
        return (self.__rad**2) * np.pi

    def __repr__(self):
        return f"The Circle has Radius: {self.__rad}, Circumference: {self.circumference()}, Area: {self.surface_area()}, Color: {self.__color}"

class Cylinder(Circle):
    def __init__(self, radius:float, height:float = 10.0, color:str = "Blue"):
        super().__init__(radius, color)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def surface_area(self):
        return super().circumference() * self.__height

    def volume(self):
        return super().surface_area() * self.__height


    def __repr__(self):
        return f"The Cylinder has Radius: {super().radius}, Height: {self.__height}, Color: {super().colour}"

class Cone(Cylinder):
    def __init__(self, radius: float, height: float = 10.0, color:str = "Blue"):
        super().__init__(radius, height, color)

    def surface_area(self):
        return (np.pi * super().radius)* (super().radius + np.sqrt((super().height**2)+(super().radius**2)))

    def volume(self):
        return (np.pi * (super().radius**2) * super().height)/3

    def __repr__(self):
        return f"The Cone has Radius: {super().radius}, Volume: {self.volume()}, Area: {self.surface_area()}, Color: {super().colour}"


if __name__ == "__main__":
    my_circle = Circle(5, "Red")
    print(my_circle)

    my_cylinder = Cylinder(5, 10, "Green")
    print(my_cylinder)

    my_cone = Cone(5, 10, "Purple")
    print(my_cone)