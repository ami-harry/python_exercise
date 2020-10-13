# faulty calculator

# exercise 2
#  45*3=55
# 56+9 =77
# 56/6=4
print("\t\t\t\tWelcome to faulty calculator")


user_inp=int(input("Enter your choice\n1. for multtplication\n2. for addition\n3 for division\n "))

if user_inp==1:
    print("You have choosen multiplication")
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    if a==45 and b==3:
        print("55")
    else:
        print(a*b)
elif user_inp==2:
    print("You have choosen aaddition")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a == 56 and b == 9:
        print("77")
    else:
        print(a + b)
elif user_inp==3:
    print("You have choosen division")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a == 56 and b == 6:
        print("4")
    else:
        print(a / b)
else:
    print("Choose a valid option")