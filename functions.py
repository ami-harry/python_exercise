'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = sum((a, b))
print("The sum is ", c)

list1 = []  # empty list
size_of_list = int(input("Enter the size of the list: "))

for data in range(size_of_list):
    print("Enter element for index no ", data, end=' ')
    list1.append(int(input(": ")))

print("the updated list is: ")
print(list1)

# printing the sum of list items
print("the sum of list items is ", sum(list1))

# inside the sum function we have to pass an iterable
# sum is an built in function


# user defined function
print()


def fun1():
    print("hello we are in function")


fun1()
fun1()
fun1()
fun1()
fun1()
fun1()
fun1()
fun1()

'''
# doc string, means it is the definition of of function, we can print it using function.__doc__
# doc string is written as """ this is doc string"""
print()

# doc string is the first line written after the function name


def func_doc(a, b):
    # """this is doct string for the function"""
    """this function will return the multiplication of two numbers"""

    return a*b


print(func_doc.__doc__)  # this will print the doc of the function
print(func_doc(54, 67))
