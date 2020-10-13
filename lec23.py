 #functions
# a=10
# b=23
# c=sum((a,b)) #sum function requires an iterable object
# print(c)
# sum is built in function

# how to make user defined function
#  def fun_name:
#      statements

# def fun1():
#     print("you are in function 1")

# without calling the function, function is useless
# fun1() #calling the function


# function taking input
# def fun(a,b):
#     print("the sum is ",a+b)
#
# fun(4,6)


# function returning something
# we have to store the returned value in a variable and can print
# def fun_ret(a,b):
#     print("the sum is ",a+b)
#     return (a+b)/2
#
# c=fun_ret(15,3)
# print("the average is ",c)


# doc_string
# doc_string --> it is about description about the function
def sum_fun(a,b):
    """this function will do the sum of two numbers
    this function desn't work for three numbers"""
    return  a+b

# printing the doc_string of the function
print(sum_fun.__doc__)
c=sum_fun(10,25)
print(c)