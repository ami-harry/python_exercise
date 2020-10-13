# self

'''
class Employee:
    no_of_leaves = 10

    # self means the objejt itself, this is automatic, this is rule of class
    def show_details(self):
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"


harry = Employee()
mohak = Employee()

harry.name = "Harry"
harry.salary = 54345
harry.role = "student"

mohak.name = "Mohak"
mohak.salary = 64342
mohak.role = "teacher"
'''

'''
print(harry.name)
print(harry.salary)
print(harry.role)
print(harry.no_of_leaves)
print()
print(mohak.name)
print(mohak.salary)
print(mohak.role)
print(mohak.no_of_leaves)

'''


'''
print(harry.show_details())  # using class method for object
print(mohak.show_details())
print(harry.no_of_leaves)
print(mohak.no_of_leaves)
mohak.no_of_leaves = 15
print(mohak.no_of_leaves)

'''


# constructor


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


e1 = Employee("harry", 238742, 21)  # passing the arguments for our constructor
e2 = Employee("mohak", 65732, 34)
print(e1.show())
print(e2.show())
