# setters or property method


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
# h2 = Employee("Mohak", "Sharma")


print(h1.Email)
# print(h2.Email)
# h1.fname = "harry"  # changing the name
# print(h1.Email)  # but the result will be same
# it will not change, becuase at the runtime creation , the constructor created with the values
# this problem can be solved by setter methods


# print(h1.Email)
h1.fname = "harry"
# here the fname will be changed, becuase the function changed with the value at runtime
# print(h1.show_email())
# here calling the email function without () becuase of @property decorator
print(h1.show_email)


# checking the setter method, that it works as per email input
h1.show_email = "this.that@gmail.com"
print("first name is ", h1.fname)
print("last name is ", h1.lname)
print("and the email is ", h1.show_email)


# deleting the email
# making deleter that will delete the email
del h1.show_email  # here the email will be deleted
print(h1.show_email)  # the it will return the condition statement

h1.show_email = "harry.hariom@gmail.com"
print(h1.show_email)
print(h1.explain)
