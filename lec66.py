# diamond shape problem(which class will use what methods, if we are facing this confusion , then this is diamond shape problem)

# diamond shape problem, means while multiple nheritance,
# java doesn;t allow multiple inheritance, C++ and Python allows it


class A:

    def met(self):
        print("This is method from class A")


class B(A):

    def met(self):
        print("This is method from class B")


class C(A):

    def met(self):
        print("This is method from class C")


class D(B, C):
    def met(self):
        print("This is method from class D")


a = A()
b = B()
c = C()
d = D()

# d.met()  # it will print method of class A(method is not overriden till)
d.met()  # it will print method of class B(method is  overriden now)
