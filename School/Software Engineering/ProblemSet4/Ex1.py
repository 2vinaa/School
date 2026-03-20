from abc import ABC, abstractmethod
from enum import Enum

import numpy as np


class ShapeType(Enum):
    CIRCLE = "Circle"
    SQUARE = "Square"
    CUBE = "Cube"
    SCALENE_TRIANGLE = "Scalene Triangle"
    RECTANGULAR_TRAPEZOID = "Rectangular Trapezoid"
    TORUS = "Torus"
    REGULAR_QUADRANGULAR_PYRAMID = "Regular Quadrangular Pyramid"


class Shape(ABC):
    def __init__(self,shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def find_area(self):
        pass

    @abstractmethod
    def print_area(self):
        pass

class Shape2D(Shape, ABC):
    def __init__(self,shape_type):
        super().__init__(shape_type)

    @abstractmethod
    def find_perimeter(self):
        pass

    @abstractmethod
    def print_perimeter(self):
        pass

class Shape3D(Shape, ABC):
    def __init__(self,shape_type):
        super().__init__(shape_type)


    @abstractmethod
    def print_volume(self):
        pass

    @abstractmethod
    def find_volume(self):
        pass



class ShapeWithEdges(Shape, ABC):
    def __init__(self,shape_type):
        super().__init__(shape_type)

    @abstractmethod
    def print_edge(self):
        pass

    @abstractmethod
    def ret_edges(self):
        pass

class ShapesWithAtleast4Vert(Shape, ABC):
    def __init__(self,shape_type):
        super().__init__(shape_type)

    @abstractmethod
    def print_vert(self):
        pass

    @abstractmethod
    def return_vert(self):
        pass

    @abstractmethod
    def ret_min_vert(self):
        pass

    @abstractmethod
    def print_min_vert(self):
        pass

class Circle(Shape2D):
    def __init__(self, radius):
        super().__init__(ShapeType.CIRCLE)
        self.__radius = radius

    def find_area(self):
        return np.pi * (self.__radius**2)

    def print_area(self):
        print(np.pi * (self.__radius**2))

    def find_perimeter(self):
        return 2*np.pi * self.__radius

    def print_perimeter(self):
        print(2*np.pi * self.__radius)

    def __repr__(self):
        return f"{self.shape_type.value}: Area : {self.find_area()}, Perimeter: {self.find_perimeter()}"

class ScaleneTriangle(Shape2D, ShapeWithEdges):
    def __init__(self, side1, side2, side3, height, edges):
        super().__init__(ShapeType.SCALENE_TRIANGLE)
        self.__base = side1
        self.__a =  side2
        self.__c = side3
        self.__height = height
        self.__number_of_edges = edges

    def find_area(self):
        return (self.__base * self.__height)/2

    def print_area(self):
        print((self.__base * self.__height)/2)

    def find_perimeter(self):
        return self.__base + self.__c + self.__a

    def print_perimeter(self):
        print(self.__base + self.__c + self.__a)

    def print_edge(self):
        print(self.__number_of_edges)

    def ret_edges(self):
        return self.__number_of_edges

    def __repr__(self):
        return f"{self.shape_type.value}: Area : {self.find_area()}, Perimeter: {self.find_perimeter()}, Number of Edge: {self.ret_edges()}"

class Square(Shape2D, ShapeWithEdges, ShapesWithAtleast4Vert):
    def __init__(self, side, edges):
        super().__init__(ShapeType.SQUARE)
        self.__side = side
        self.__number_of_edges = edges

    def print_vert(self):
        print(self.__side)

    def return_vert(self):
        return self.__side

    def ret_min_vert(self):
        return self.__side

    def print_min_vert(self):
        print(self.__side)

    def find_area(self):
        return self.__side**2

    def print_area(self):
        print(self.__side**2)

    def find_perimeter(self):
        return self.__side*4

    def print_perimeter(self):
        print(self.__side*4)

    def print_edge(self):
        print(self.__number_of_edges)

    def ret_edges(self):
        return self.__number_of_edges

    def __repr__(self):
        return f"{self.shape_type.value}: Area : {self.find_area()}, Perimeter: {self.find_perimeter()}, Number of Edge: {self.ret_edges()}, Min Vert: {self.ret_min_vert()}"

class Cube(Shape3D, ShapeWithEdges, ShapesWithAtleast4Vert):
    def __init__(self, side, edges):
        super().__init__(ShapeType.CUBE)
        self.__side = side
        self.__number_of_edges = edges

    def print_vert(self):
        print(self.__side)

    def return_vert(self):
        return self.__side

    def ret_min_vert(self):
        return self.__side

    def print_min_vert(self):
        print(self.__side)

    def find_volume(self):
        return self.__side**3

    def print_volume(self):
        print(self.__side**3)

    def find_area(self):
        return (self.__side**2)*6

    def print_area(self):
        print((self.__side**2)*6)

    def print_edge(self):
        print(self.__number_of_edges)

    def ret_edges(self):
        return self.__number_of_edges

    def __repr__(self):
        return f"{self.shape_type.value}: Volume: {self.find_volume()}, Area: {self.find_area()}, Number of Edge: {self.ret_edges()}, Min Vert: {self.ret_min_vert()}"

if __name__ == "__main__":
    print("=== Testing Circle ===")
    # Requires: radius
    my_circle = Circle(radius=5)
    print(my_circle)
    print("Calling print_area():", end=" ")
    my_circle.print_area()

    print("\n=== Testing Scalene Triangle ===")
    # Requires: side1 (base), side2, side3, height, edges
    my_triangle = ScaleneTriangle(side1=4, side2=5, side3=6, height=4.5, edges=3)
    print(my_triangle)
    print("Calling print_edge():", end=" ")
    my_triangle.print_edge()

    print("\n=== Testing Square ===")
    # Requires: side, edges
    my_square = Square(side=4, edges=4)
    print(my_square)
    print("Calling print_vert():", end=" ")
    my_square.print_vert()

    print("\n=== Testing Cube ===")
    # Requires: side, edges
    my_cube = Cube(side=3, edges=12)
    print(my_cube)
    print("Calling print_volume():", end=" ")
    my_cube.print_volume()