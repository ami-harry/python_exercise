# exercise 5
# health managemnt system

# make 3 file to store the food details \t 3 files to store exercise details
# write a function that will take argument as client name \t will ask what you want to store, 1--> food \t 2 for exercise
# store the details into seperated files

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program


import datetime


def gettime():
    return datetime.datetime.now()


def save_details(opt):
    if opt == 1:
        d = int(input("Enter 1 for food \t 2 for snacks \t 3 for breakfast\n"))
        if d == 1:
            data = input("Enter food for harry\n")
            with open("Harry_food.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("food details for harry saved sucessfully")
        elif d == 2:
            data = input("Enter snacks for harry\n")
            with open("Harry_snacks.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("snacks details for harry saved sucessfully")
        elif d == 3:
            data = input("Enter  breakfast for harry\n")
            with open("Harry_breakfast.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("breakfast details for harry saved sucessfully")
        else:
            print("Enter valid options")
    elif opt == 2:
        d = int(input("Enter 1 for food \t 2 for snacks \t 3 for breakfast\n"))
        if d == 1:
            data = input("Enter food for Alok\n")
            with open("Alok_food.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("food details for Alok saved sucessfully")
        elif d == 2:
            data = input("Enter snacks for alok\n")
            with open("Alok_snacks.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("snacks details for alok saved sucessfully")
        elif d == 3:
            data = input("Enter  breakfast for alok\n")
            with open("Alok_breakfast.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("breakfast details for Alok saved sucessfully")
        else:
            print("Enter valid options")
    elif opt == 3:
        d = int(input("Enter 1 for food \t 2 for snacks \t 3 for breakfast\n"))
        if d == 1:
            data = input("Enter food for Mayank\n")
            with open("Mayank_food.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("food details for Mayank saved sucessfully")
        elif d == 2:
            data = input("Enter snacks for Mayank\n")
            with open("Mayank_snacks.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("snacks details for Mayank saved sucessfully")
        elif d == 3:
            data = input("Enter  breakfast for Mayank\n")
            with open("Mayank_breakfast.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("breakfast details for Mayank saved sucessfully")
        else:
            print("Enter valid options")
    elif opt == 4:
        d = int(input("Enter 1 for food \t 2 for snacks \t 3 for breakfast\n"))
        if d == 1:
            data = input("Enter food for Pandey\n")
            with open("Pandey_food.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("food details for Pandey saved sucessfully")
        elif d == 2:
            data = input("Enter snacks for Pandey\n")
            with open("Pandey_snacks.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("snacks details for Pandey saved sucessfully")
        elif d == 3:
            data = input("Enter  breakfast for Pandey\n")
            with open("Pandey_breakfast.txt", "a") as hf:
                hf.write(str([str(gettime())])+": " + data + "\n")
            print("breakfast details for Pandey saved sucessfully")
        else:
            print("Enter valid options")
    else:
        print("Enter valid option")


def show_details(b):
    if b == 1:
        d = int(input("Enter 1 for food \t 2 for snacks \t 3 for breakfast"))
        if d == 1:
            with open("Harry_food.txt") as hf:
                for data in hf:
                    print(data)
                print("food details of harry printed sucessfully")
        elif d == 2:
            with open("Harry_snacks.txt") as hf:
                for data in hf:
                    print(data)
                print("snacks details of harry printed sucessfully")
        elif d == 3:
            with open("Harry_breakfast.txt") as hf:
                for data in hf:
                    print(data)
                print("breakfast details of harry printed sucessfully")
        else:
            print("Enter valid options")
    elif b == 2:
        d = int(input("Enter 1 for food \t 2 for snacks \t 3 for breakfast"))
        if d == 1:
            with open("Alok_food.txt") as hf:
                for data in hf:
                    print(data)
                print("food details of alok printed sucessfully")
        elif d == 2:
            with open("Alok_snacks.txt") as hf:
                for data in hf:
                    print(data)
                print("snacks details of alok printed sucessfully")
        elif d == 3:
            with open("Alok_breakfast.txt") as hf:
                for data in hf:
                    print(data)
                print("breakfast details of alok printed sucessfully")
        else:
            print("Enter valid options")
    elif b == 3:
        d = int(input("Enter 1 for food \t 2 for snacks \t 3 for breakfast"))
        if d == 1:
            with open("Mayank_food.txt") as hf:
                for data in hf:
                    print(data)
                print("food details of mayank printed sucessfully")
        elif d == 2:
            with open("Mayank_snacks.txt") as hf:
                for data in hf:
                    print(data)
                print("snacks details of mayank printed sucessfully")
        elif d == 3:
            with open("Mayank_breakfast.txt") as hf:
                for data in hf:
                    print(data)
                print("breakfast details of Mayank printed sucessfully")
        else:
            print("Enter valid options")
    elif b == 4:
        d = int(input("Enter 1 for food \t2 for snacks \t 3 for breakfast\n"))
        if d == 1:
            with open("Pandey_food.txt") as hf:
                for data in hf:
                    print(data)
                print("food details of Pandey printed sucessfully")
        elif d == 2:
            with open("Pandey_snacks.txt") as hf:
                for data in hf:
                    print(data)
                print("snacks details of Pandey printed sucessfully")
        elif d == 3:
            with open("Pandey_breakfast.txt") as hf:
                for data in hf:
                    print(data)
                print("breakfast details of Pandey printed sucessfully")
        else:
            print("Enter valid options")
    else:
        print("Enter valid option")


print("\t\t\t\tWelcome to health management system")
ch = int(input("Enter 1 to save details \t 2 to see the details\n"))
if ch == 1:
    b = int(input("Enter 1 for Harry \t2 for Alok\t3 for Mayank\t4 for Pandey\n"))
    save_details(b)
elif ch == 2:
    b = int(input("Enter 1 for Harry \t2 for Alok\t3 for Mayank\t4 for Pandey\n"))
    show_details(b)
else:
    print("Enter valid options")
