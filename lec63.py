# public(PubVarName)
# private (__PvtVarName)
# protected (_PrtVarName)

# to access the protected variable , instance._PrtVarName
# to access the private variable , instance._ClassName.__PvtVarName


class Student():
    no_of_students = 10
    _PrtVar = "hey this is protected variable"
    __PvtVar = "this is private variable"
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


s1 = Student("harry", 21, 54)
s2 = Student.constructor_class("mohak-34-65")

# private and protected variable can be used by main classes and only by those classes from which they are inherited

print(s1._PrtVar)
print(s2._PrtVar)

print(s1._Student__PvtVar) #accessing private variable
print(s2._Student__PvtVar)

# we will felt name mangling in python, so we must use _class name to access that variable