'''
# factorial using iterative method

ch = int(input("Enter 1 to use for loop\nEnter 2 to use while loop\n"))

if ch == 1:
    def rec_fun(num):
        fac = 1
        for i in range(num):
            fac = fac*(i+1)
        return fac

elif ch == 2:
    def rec_fun(num):
        fac = 1
        i = 1
        while i in range(num):
            fac = fac*(i+1)
            i += 1
        return fac

else:
    print("Enter a valid choice\n")
    exit(0)

number = int(input("Enter the number: "))
print("Factorial using iterative method is ", rec_fun(number))
'''

'''

# factorial using recursive method/function

def recursive_fun(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * recursive_fun(num-1)


number = int(input("Enter the number: "))
print("Factorial using recursive method is ", recursive_fun(number))

'''


# fibonacii series upto n


def fibonacii_of_num(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacii_of_num(num-1)+fibonacii_of_num(num-2)


number = int(input("Enter the number: "))
print("the fibonacii is ", fibonacii_of_num(number))
