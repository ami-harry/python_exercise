# instance variable and class variable


class Employee:
    no_of_leaves = 10
    pass


harry = Employee()
mohak = Employee()

harry.name = "Harry"
harry.salary = 54345
harry.role = "student"

mohak.name = "Mohak"
mohak.salary = 64342
mohak.role = "teacher"


print(harry.name)
print(harry.salary)
print(harry.role)
print(harry.no_of_leaves)
print()
print(mohak.name)
print(mohak.salary)
print(mohak.role)
print(mohak.no_of_leaves)

# instance variable is the property of the object itself.
# class variable is availabe for all and we cant change it directly, or instance variable cann't change it.

# no_of_leaves is class variable
# harry.name is instance variable

# we cant change no_of_leaves using instance variable, or instance object,,,
# before changing
print(Employee.no_of_leaves)
print(Employee.__dict__)
print()
# changing no of leaves using instance object

# we use __dict__ to check instance variable
# before trying to change the class variable
print(mohak.__dict__)
mohak.no_of_leaves = 15  # it will create new instance variable for instance object
# after changing
print(mohak.__dict__)

# it will not be changes , it will remain same as it was
# after changing
print()
print(Employee.no_of_leaves)
print(Employee.__dict__)
