# object introspection
# to know about the object, location, id and all

import inspect


class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.Email = f"The email is {self.fname}.{self.lname}@gmail.com"

    @property
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property  # by using property decorator, we can use this method as a normal property as fname, lname
    def show_email(self):
        if self.fname == None or self.lname == None:
            return "email is not set, please set it using setter"
        return f"The email is {self.fname}.{self.lname}@gmail.com"

    # making a function that will take email as input and will change fname and lname as per input
    @show_email.setter
    def show_email(self, string):
        print("setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @show_email.deleter  # when this will be called, the email will be deleted
    def show_email(self):
        self.fname = None
        self.lname = None


h1 = Employee("Hariom", "Kumar",)
h2 = Employee("harry", "Kumar",)

# print(h1.show_email)
# print(type("this is string"))
# print(type(h1))
# print(id(h1))
# print(type(h2))
# print(id(h2))
# a = "this is harry"
# print(dir(a))
# print(dir(h1)) #operations that we can perform

# print(inspect.getmembers(h1))
