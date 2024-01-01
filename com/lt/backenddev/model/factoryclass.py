"""
工厂类
"""
class Person:
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

class FactoryClass:
    def getPerson(self,type):
        if type == "Student":
            return Student()
        elif type == "Teacher":
            return Teacher()
        else:
            return None