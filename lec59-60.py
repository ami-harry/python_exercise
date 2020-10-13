# abstraction(kisi kam ko parts me break kr dena)
# enscaptulation(hiding details)


# inheritance
# -->getting additional features from parents, or inherits the features


class Student():
    no_of_students = 10

    # constructor
    def __init__(self, s_name, s_roll, s_marks):
        self.name = s_name
        self.roll = s_roll
        self.marks = s_marks

    # method to show the details
    def show_details(self):
        print(
            f"Student name is {self.name}, roll is {self.roll} and marks is {self.marks}")

    # class method to change the no of students
    @classmethod
    def total_students(cls, new_students):
        cls.no_of_students = new_students

    # class method////alternative constructor
    @classmethod
    def constructor_class(cls, str):
        return cls(*str.split("-"))

    # normal class method
    @classmethod
    def good_str(cls, str):
        return f"{str} is returning"

    @staticmethod
    def stat_meth(str):
        return f"{str} is returning from static method"


'''
s1 = Student("harry", 21, 54)
s2 = Student.constructor_class("mohak-34-65")
print(Student.show_details(s1))
print(Student.show_details(s2))
print(Student.good_str("hey this is hariom "))
# print(Student.__dict__)
print(Student.no_of_students)
s1.total_students(25)
print(Student.no_of_students)

'''


# single inheritance

# a class is inherit from another  class, then the new class has all the features of its parent class, and this can also access and use all the method and it can have its own new method and others can also inherit from this class

'''
class Programmer(Student):
    pass
# this means the class programmer is inherited from student , this can also use all the methods and attributes of its parent class


# s1 = Student("harry", 21, 54)
# s2 = Student.constructor_class("mohak-34-65")
# print(Student.show_details(s1))
# print(Student.no_of_students)
# s1.total_students(25)

# s3 = Programmer("nitish", 38, 85)
# s4 = Programmer.constructor_class("ronik-35-82")
# print(Programmer.show_details(s3))
# print(Programmer.show_details(s4))
# print(Programmer.show_details(s3))
# print(Programmer.show_details(s4))
# print(Programmer.no_of_students)

# s3.show_details()

'''


class Programmer(Student):

    # constructor method its own class
    # here we are not using super()
    def __init__(self, s_name, s_roll, s_marks, p_id, p_sal, languages):
        self.name = s_name
        self.roll = s_roll
        self.marks = s_marks
        self.id = p_id
        self.salary = p_sal
        self.lang = languages

    def show_prog(self):
        print(
            f"the programmer name is {self.name}, roll is {self.roll}, marks is {self.marks}, id is {self.id} ,salary is {self.salary}, and he knows {self.lang}")


# s1 = Student("nitish", 38, 85)
# s2 = Programmer.constructor_class("ronik-35-82")
# Programmer.show_prog(s1)

p1 = Programmer("hariom", 21, 67, 545, 877554, ["pyhon,java,web,data science"])
p2 = Programmer("jenny", 12, 91, 236, 287732, ["web, js,angular, react"])
p1.show_prog()
p2.show_prog()
# p1.show_details()
print(p1.stat_meth("hey "))#calling static method using instance