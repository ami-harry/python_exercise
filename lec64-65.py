# polymorphism

# abality to take various forms

# polymorphism
# abstraction
# emscaptulation
# inheritance


# overiding
# super()


class A:
    classvar1 = "I am a class variable in class A"

    # instance method
    def __init__(self):
        self.var1 = " i am a constructor in class A"
        self.classvar1 = "i am a instance var in class A"
        self.special = "i am special hai bhai A ka"


class B(A):
    classvar2 = "I am a class variable in class B"


# method overriding


    def __init__(self):
        super().__init__() #calling the super() method here, it will run first, the program from will go to first class first, then it will return to this class
        self.var1 = " i am a constructor in class B"
        self.classvar1 = "i am a instance var in class B"
        self.special = "i am special hai bhai B ka"
        # calling the constructor  of class A
        # super().__init__()
        # print(super().special)


a = A()
b = B()

# print(a.special)
# first it will find this var in class B, if not found the it willl goto its parent class
# print(b.classvar1)
# print(b.classvar2)
# method overiding
# if both the classes have the constructor, then the lastest class will get more priority, if we want to access the variables of father class, then we have to use super() method, while calling the super() method, order of calling will also matter, flow of program also depends upon the output

print(b.special)
print(b.classvar1)
