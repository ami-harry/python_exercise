# class and its methods 

class Student:
    assignments = 5  # class variable

    # making constructor
    def __init__(self, st_name, st_roll, st_sem):
        self.name = st_name
        self.roll = st_roll
        self.sem = st_sem

    # instance method to show the values
    def show(self):
        print(
            f"Name is {self.name}, roll is {self.roll} and semester is {self.sem}")

    # class method to change the class variable using instance (class method as alternative constructor)
    @classmethod
    def change_assignment(cls, new_assignment):
        cls.assignments = new_assignment

    # another class method like constructor, this will work as same as the constructor(class method as alternative constructor)
    # making instances from string having -
    @classmethod
    def ins_from_dash(cls, str):
        args = str.split("-")
        print(args)  # this will return a list
        return cls(args[0], args[1], args[2])

    # making a class method to work like constructor , it will make instance with string having spaces
    @classmethod
    def ins_from_space(cls, str):
        args = str.split(" ")
        return cls(*args)

    # making a class method to work like constructor, it will make instance with string having commas
    @classmethod
    def ins_from_comma(cls, str):
        return cls(*str.split(","))


s1 = Student("hariom", 21, 2)  # instance using constructor
s2 = Student.ins_from_comma("alok,05,3")  # instance using class method
s3 = Student.ins_from_dash("mayank-34-1")  # instance using class method
s4 = Student.ins_from_space("pandey 73 6")  # instance using class method

s1.show()
s2.show()
s3.show()
s4.show()

print("original class variable", s1.assignments)
s1.change_assignment(15)  # using class method
print("after modification class variable", Student.assignments)
