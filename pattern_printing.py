# take a input and ask the bool no. if 1 then print the start in increasing order else decreasing order

num = int(input("How many rows you want to print: "))  # asking
boolean = int(
    input("Enter 1 for increasing order and 0 for decreasing order: "))

if boolean == 1:
    for i in range(1, num+1):
        for j in range(1, i+1):
            print('*', end="")
        print()
elif boolean == 0:
    for i in range(num, 0, -1):
        for j in range(1, i+1):
            print('*', end="")

        print()

else:
    print("Enter valid input")
