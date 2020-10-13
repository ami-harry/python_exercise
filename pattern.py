ch = int(input("Enter 1 for using for loop\nEnter 2 for using while loop\n"))

num = int(input("Enter how many line you want to print: "))

bool_inp = int(input(
    "Enter 1 to print in increasing order\nEnter 2 to print in decreasing order\n"))

# using for loop
if ch == 1:
    if bool_inp == 1:
        for i in range(num):
            for j in range(i+1):
                print("*", end='')
            print()
elif bool_inp == 0:
    for i in range(num, 0, -1):
        for j in range(1, i+1):
            print("*", end='')
        print()


# using while loop

if ch == 2:
    if bool_inp == 1:
        i = 0
        while i in range(num):
            j = 0
            while j in range(i+1):
                print("*", end='')
                j += 1
            i += 1
            print()
    elif bool_inp == 2:
        i = 1
        while i in range(1, num+1):
            j = i
            while j in range(num, 0, -1):
                print("*", end='')
                j += 1
            print()
            i += 1

else:
    print("Enter correct input")


'''
# i = 1
# while i in range(1, num+1):
#     j = i
#     while j in range(num, 0, -1):
#         print('*', end='')
#         j += 1
#     i += 1
#     print()


# for i in range(num):
#     for j in range(i+1):
#         print("*", end='')
#     print()

# for i in range(num, 0, -1):
#     for j in range(1, i+1):
#         print("*", end='')
#     print()

i = 1
while i in range(1, num+1):
    j = i
    while j in range(num, 0, -1):
        print("*", end='')
    print()
    i += 1

'''
