num = int(input("Enter the number: "))
boolean = int(input("Enter 1 for True and 0 for Flase: "))

if boolean == 1:
    for i in range(num):
        for j in range(i):
            print('*', end="")
        print('\n')
elif boolean == 0:
    for i in range(1):
        for j in range(num):
            print('*', end='')
        print('\n')
else:
    print("Enter valid input")
