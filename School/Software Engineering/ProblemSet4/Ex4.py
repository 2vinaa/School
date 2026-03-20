class Person():
    def __init__(self, name: str, last_name:str):
        self.__name = name
        self.__surname = last_name

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    def __repr__(self):
        return f"Person: {self.__name} {self.__surname}"


class Student(Person):
    def __init__(self,name:str, surname:str,reg_number:int):
        Person.__init__(self,name,surname)
        self.__reg_num = reg_number

    @property
    def registration_number(self):
        return self.__reg_num

    def __repr__(self):
        return f"Student: {self.name} {self.surname}, Registration Number: {self.registration_number}"


class Worker(Person):
    def __init__(self,name:str, surname:str,salary:int):
        Person.__init__(self,name,surname)
        self.__monthly_salary = salary

    @property
    def salary(self):
        return self.__monthly_salary

    def __repr__(self):
        return f"Worker: {self.name} {self.surname}, Monthly Salary: {self.__monthly_salary}"



class StudentWorker(Student,Worker):
    def __init__(self, name:str, surname:str, reg_num:int, salary:int):
        Student.__init__(self,name,surname,reg_num)
        Worker.__init__(self, name, surname, salary)

    def __repr__(self):
            return f"StudentWorker: {self.name} {self.surname}, Registration Number: {self.registration_number}, Monthly Salary: {self.salary}"




if __name__ == "__main__":

    people = [] #list[Person]
    p = Person("John", "Doe")
    people.append(p)

    s = Student("Alice", "Smith", 12345)
    people.append(s)

    w = Worker("Bob", "Johnson", 5000)
    people.append(w)

    sw = StudentWorker("Charlie", "Brown", 67890, 3500)
    people.append(sw)

    for i in people:
        print(i)