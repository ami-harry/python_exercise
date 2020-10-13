# operator overloading
# dunder method(__MethodName__)


class Employee():

    no_of_leaves = 10

    # constructor
    def __init__(self, ename, eid, esal, pos):
        self.name = ename
        self.id = eid
        self.sal = esal
        self.position = pos

    # instance method
    def Show_details(self):
        return f"Employee name is {self.name}, id is {self.id} ,position is {self.position} and salary is {self.sal}"

    @classmethod
    def change_leaves(cls, new_leave):
        cls.no_of_leaves = new_leave

    # method to resolve operator overloading
    def __add__(self, other):
        return self.sal + other.sal

    def __truediv__(self, other):
        return self.sal/other.sal


e1 = Employee("Hariom", 'emp1', 80, "programmer")
e2 = Employee("Mohak", 'emp2', 40, "swipper")
# print(e1+e2)#this is operator overloading, if we don't have any method before

# now we have a __add__ (dander)method, which will add the salary of two employees, or instanes

print(e1+e2)  # addition(+)
print(e1/e2)  # true division(/)


