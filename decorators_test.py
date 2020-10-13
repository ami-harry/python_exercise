# decorators ,
# function calling a function inside execution of another function
from time import sleep

'''

def fun1(fun2):
    def inner_exe():
        print("fun1 is executing")
        sleep(2)
        print("going to fun2")
        sleep(2)
        fun2()
        print("returned from fun2")
        sleep(2)
        print("fun1 executed sucessfully")
    return inner_exe()


def fun2(fun3):
    def runner():
        print("fun2 is calling")
        sleep(2)
        print("fun3 is calling inside fun2")
        sleep(2)
        fun3()
        sleep(2)
        print("fun3 called sucessfully")
        sleep(2)
        print("going back to fun1")
    return runner


def fun3():
    def runner():
        print("This is fun3")
        print("fun3 over")
    return runner


# fun = fun1(fun2(fun3()))
fun = fun1(fun2(fun3()))
fun

'''


# or we can do it in easy way


def fun1(a):
    def inner_exe():
        print("fun1 is executing")
        sleep(2)
        print("going to fun2")
        sleep(2)
        a()
        print("returned from fun2")
        sleep(2)
        print("fun1 executed sucessfully")
    return inner_exe()


@fun1
def fun2():
    print("this is printing")


@fun1
def fun3():
    print("this is another function")
