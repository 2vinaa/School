
from Prog.Sphere.sphere import Sphere


if __name__ == "__main__":
    s1 = Sphere(17) #S1 == Instance one
    print(f"the surface of s1 {s1.surface()}")
    print(f"the volume of s1 { s1.volume()}")

    s2 = Sphere(4)
    print(f"the surface of s2 {s2.surface()}")
    print(f"the volume of s2 {s2.volume()}")


    #or

    print(s1) #they only work due to __repr__ in the other file (sphere.py)
    print(s2)
