# local and global variable

'''
a = 10


def fun(n):
    a = 5  # local variable for this function

    # we cant change the global variable inside the function
    # for this we have to use global keyword
    print(n, " this is printting")
    print(a)


fun("harry ")

'''

'''
# nested function


def fun1():
    x = 10

    def fun2():
        global x  # it will look for global variable outside the functions, but there is no global variable, so the value will remain same
        x = 40
    print("before calling fun2()", x)
    fun2()
    print("After calling fun2()", x)


fun1()

'''
'''


# nested function using global variable
x = 5


def fun1():
    x = 50

    def fun2():
        global x  # here it will modify the x value, becuase global x is present
        print("The global variable before modification is ", x)
        x = x+10
        print("The global variable after modification is ", x)

    # this line will access the local variable of fun1()
    print("Before calling fun2() local x is", x)
    fun2()
    # this line will access the local variable of fun1()
    print("After calling fun2() local x is", x)


fun1()
# this will print the modified value of x
print("after function call the global x is ", x)

'''