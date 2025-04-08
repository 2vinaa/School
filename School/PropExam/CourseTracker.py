


class CourseMap:
    def __init__(self):
        self.courses = []

    def __str__(self):
        return str(self.courses)

    def put(self, code, name):
        self.courses.append([code, name])

    def getname(self, code):
        for element in self.courses:
            if element[0] == code:
                return element[1]
            else:
                pass
        return "This code isnt in the database"

    def removefromcode(self,code):
        for element in self.courses:
            if element[0] == code:
                self.courses.remove(element)
                return "The course has been removed"
            else:
                pass
        return "The course wasnt in the DB"


    def printall(self):
        for element in self.courses:
            print(f"{element[0]}:{element[1]}")
            




if __name__ == "__main__":
    a = CourseMap()

    a.put("CS101", "Intro to CS")
    a.put("MATH100", "Calculus I")
    a.put("ENG200", "English Literature")

    print(a)

    print(a.getname("CS101"))
    print(a.getname("saaase"))
    print(a.removefromcode("ENG200"))
    a.printall()

