import datetime

def gettime():
    return datetime.datetime.now()


def data_inp(choice):
    if choice == 1:
        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Harry_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Harry_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Harry_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")

    elif choice == 2:
        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Mayank_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Mayank_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Mayank_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")

    elif choice == 3:
        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Alok_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Alok_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Alok_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")
    else:
        print("Please enter valid input\n")


def data_out(choice):
    if choice == 1:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Harry_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Harry_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Harry_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')

    elif choice == 2:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Mayank_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Mayank_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Mayank_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')
    elif choice == 3:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Alok_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Alok_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Alok_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')
    else:
        print("Enter a valid input\n")


print("\t\tWelcome to health management system")

add_see = int(input("Enter 1 to add details\nEnter 2 to see the details\n"))

if add_see == 1:
    usr_name = int(input(
        "Enter\n1 for Harry\n2 For Mayank\n3 for Alok\n"))  # \n4 for Prakash\n5 for Mohak\n6 for Nitish"))
    data_inp(usr_name)
else:
    usr_name = int(input(
        "Enter\n1 for Harry\n2 For Mayank\n3 for Alok\n"))  # \n4 for Prakash\n5 for Mohak\n6 for Nitish"))
    data_out(usr_name)
