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

    # one liner method
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))  # using args concept here


'''
    # using this class method we are making out i
    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        print(params)  # this will give the list
        # the splited string will be in list and with index no we are making object, this is lternative constructor
        return cls(params[0], params[1], params[2])
'''


e1 = Employee("harry", 238742, 21)  # passing the arguments for our constructor
e2 = Employee("mohak", 65732, 34)

# performing the same task of constructor using class method

# the split method will change this string into list and that after it will work
# e3 = Employee.from_str("alok-64732-45")
e3 = Employee.from_dash("alok-64732-45")


print(e1.show())
print(e2.show())
print(e3.show())  # this will work now
# print(Employee.no_of_leaves)
# here we can  change the class variable using class method by instance variable
# e1.change_leaves(50)
# print(Employee.no_of_leaves)
