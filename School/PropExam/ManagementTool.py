import datetime


class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def __str__(self):
        return f"This is the students name {self.name}, Their age {self.age} and their grades {self.grades}"

    def add_grades(self, course, value):
        grade = Grade(value, course, datetime.date)
        self.grades.append(grade)



class Grade:
        def __init__(self, value, course, student):
                self.value = value
                self.course = course
                self.date = datetime.date
                self.student = student

        def __str__(self):
            return f"{self.value}, {self.course}, {self.date}, {self.student}"



class Course:
    def __init__(self, name):
        self.name = name
        self.listofcourses = []


    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":








