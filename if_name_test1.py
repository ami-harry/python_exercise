def testFun():
    print("This is function of test file")


def sum1(a, b):
    """this function works for two integers, it will not work for theree

    Args:
        a (int): the input should be an integer
        b (int): the input should be an integer
    """
    print("This function will print sum of two numbers")
    print("the sum is ", a+b)


'''
testFun()
sum1(10, 15)
print(sum1.__doc__)
print("this is a normal print statement in this file")
print("this line will be printed if this file will import into another file ")

'''


if __name__ == "__main__":
    sum1(10, 20)
    print(sum1.__doc__)
    testFun()
    print("these lines will not print in another file if we import this file into that file")
