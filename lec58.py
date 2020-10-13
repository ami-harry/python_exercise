# static method
# class method


class Employee:
    no_of_leaves = 10

    # this is constructor(constructor method)
    def __init__(self, Iname, Isalary, Irole):
        self.name = Iname
        self.salary = Isalary
        self.role = Irole

    # instance method
    def show(self):
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

    # class method, this will allow to change the class variable using instance
    # class method as alternative constructor
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves  # changing the old leaves value with new one

    # one liner method _alternative constructor
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))  # using *args concept here

# static method is used to make those functions can only be used with class and objects only
    @staticmethod
    def good_fun(string):
        return f"this {string} is returned"


e1 = Employee("harry", 238742, 21)  # passing the arguments for our constructor
e2 = Employee("mohak", 65732, 34)
e3 = Employee.from_dash("alok-64732-45")

print(e1.show())
print(e2.show())
print(e3.show())

print(Employee.good_fun("hiii"))  # calling static method

print(e1.good_fun("okk"))
