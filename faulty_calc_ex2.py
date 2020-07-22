# you have to make a faulty calculator
# it will give wrong answer for some calculations

# 45*3=555
# 56+9=77
# 56/6=4

# take input from user...which operator you want to perform


choice = int(input(
    "enter your choice:\n1 for addition\n2 for multiplication\n3 for division\n"))


if choice == 1:
    print("you have choosen the addition")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second  number: "))
    if num1 == 56 and num2 == 9:
        print("The sum is 77")
    else:
        print("The sum is ", num1+num2)

elif choice == 2:
    print("you have choosen the multiplication")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second  number: "))
    if num1 == 45 and num2 == 3:
        print("The multiplication is 555")
    else:
        print("The multiplication is ", num1*num2)

elif choice == 3:
    print("you have choosen the division")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second  number: "))
    if num1 == 56 and num2 == 6:
        print("The divisiom is 4")
    else:
        print("The divisiom is ", num1/num2)

else:
    print("invalid choice")
