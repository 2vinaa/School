from enum import Enum
from typing import List


class Person:
    def __init__(self, first_name: str, last_name: str, year_of_birth : int):
        self.name = first_name
        self.surname = last_name
        self.yob = year_of_birth
        self.age = 0

    def get_age(self):
        self.age = 2026 - self.yob
        return self.age

    def __repr__(self):
        return f"First Name: {self.name}, Last Name: {self.surname}, Year of Birth : {self.yob}, Age: {self.age}"

class Course:
    class WeekDay(Enum):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

    def __init__(self, name:str, instructor:str, DayOfWeek:WeekDay):
        self.CourseName = name
        self.CourseInstructor = instructor
        self.CourseDay = DayOfWeek
        self.subscribers = []

    def add_sub(self, subscriber):
        self.subscribers.append(subscriber)

    def __repr__(self):
        return f"Course Name: {self.CourseName}, Instructor: {self.CourseInstructor}, Day: {self.CourseDay}, Subscribers: {self.subscribers}"

class Gym:
    def __init__(self, courses: List[Course], members: List[member]):
        self.courses = courses
        self.members = members

        for i in self.courses:
            i.subscribers = [j for j in i.subscribers if j in self.members]


