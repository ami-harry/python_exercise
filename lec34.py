# recursion

# function calling itself
'''
def fun1(my_str):
    print("The string is ", my_str)
    fun1(my_str)  # calling function inside function


fun1("This is recursive function")
# this will be get exit at 996 times of execution

'''


# finding factorial
'''
# iterative method
def fun1(num):
    fact = 1
    for i in range(num):
        fact = fact*(i+1)
    return fact


n = int(input("Enter the number"))
print(fun1(n))

'''
'''


# recursive method
def fun1(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*fun1(num-1)


n = int(input("Enter the number"))
print(fun1(n))

'''


# quiz
'''
# finobachii series

# 0 1 1 2 3 5 8 13 21

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


a = int(input("Enter the number "))
print(fib(a))

'''

# fibonacii series using iterative method


def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


for i in range(10):
    print(f(10))
