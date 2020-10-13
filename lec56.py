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
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves


e1 = Employee("harry", 238742, 21)  # passing the arguments for our constructor
e2 = Employee("mohak", 65732, 34)
print(e1.show())
print(e2.show())
print(Employee.no_of_leaves)
# here we can  change the class variable using class method by instance variable
e1.change_leaves(50)
print(Employee.no_of_leaves)
