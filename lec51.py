import time
# decorators


'''
def fun1():
    print("hello harry")


fun2 = fun1 #copying the function into another, without calling the funciton
del fun1  # here we are deleting the previous function, but fun2 will work
fun2()

'''
'''


def funret(num):
    if num == 0:
        return print
    if num == 1:
        return sum


a = funret(0)  # function returning function
b = funret(1)
print(a)
print(b)
# a function can return another function

'''
'''


# function executing the function as its parameter
def exec(fun):
    fun("this is printing")


exec(print)

'''


# decorators


'''
def dec1(func1):
    def nowexec():
        print("Executing decorator function now")
        time.sleep(2)
        func1()
        time.sleep(2)
        print("decorator function executed sucessfully")
    return nowexec


def who_is_harry():
    print("execution coming from decorators to another function")
    time.sleep(2)
    print("harry is a good boy")
    time.sleep(2)
    print("execution going back to decorators from another function")


# who_is_harry()
# who_is_harry = dec1(who_is_harry)
# this concept is called decorators (@)
# who_is_harry()
# we can put @fun_name at top of the another function

'''


def dec1(func1):
    def nowexec():
        print("Executing decorator function now")
        time.sleep(2)
        func1()
        time.sleep(2)
        print("decorator function executed sucessfully")
    return nowexec


@dec1
def who_is_harry():
    print("execution coming from decorators to another function")
    time.sleep(2)
    print("harry is a good boy")
    time.sleep(2)
    print("execution going back to decorators from another function")


who_is_harry()

# decorators is used when we want to use a function many times before another function
