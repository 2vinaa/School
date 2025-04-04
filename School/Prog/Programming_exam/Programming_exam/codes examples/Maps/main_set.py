from set import Set

if __name__ == '__main__':
    smith = Set()
    smith.add("CSCI-112")
    smith.add("MATH-121")
    smith.add("HIST-340")
    smith.add("ECON-101")

    roberts = Set()
    roberts.add("POL-101")
    roberts.add("ANTH-230")
    roberts.add("CSCI-112")
    roberts.add("ECON-101")

    print("Smith:", smith)
    print("Roberts:", roberts)

    # Intersection
    common_courses = smith.intersection(roberts)
    print("Common courses:", common_courses)

    # Difference
    unique_courses = smith.difference(roberts)
    print("Courses unique to Smith:", unique_courses)