# try and except
# if try is failed or any error then to save the program from exit
# we use try and expect, we usually catch the error and then print it as as string adn after that our next statements will be printed

# suppose it we are making a program of sum of two number and if user inputs an string so here it will through an error,, we will catch that error and will save the program


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

a = (input("Enter a: "))  # here the input is in string
b = (input("Enter b: "))  # here the input is in string
# print("the sum is ", int(a)+int(b))
# here we are changing the numebrs into the int

# if user inputs a string then it will through an error, so we are printing the error as string and program will save
try:
    print("the sum is ", int(a)+int(b))
    # we are trying if the program can execute it and if error occurs then we are catching the error

except Exception as hk:
    print(hk)

print("This is out of try and except ")