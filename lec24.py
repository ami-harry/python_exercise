# try except

# exception handling

#
num1=input("Enter the number: ")
num2=input("Enter the number: ")

# print(num1+num2)
#suppose if we give wrong input, this wil give error, so we will except the error
try:
    print(int(num1)+int(num2))
except Exception as e:
    print(e) #the error will be printed as string and our program will run sommthly without any interruption
print("this line is very important")
