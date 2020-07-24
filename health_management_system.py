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

    elif choice == 4:

        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Mohak_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Mohak_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Mohak_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")

    elif choice == 5:

        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Prakash_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Prakash_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Prakash_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")

    elif choice == 6:

        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Nitish_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Nitish_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Nitish_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")

    elif choice == 7:

        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Ronik_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Ronik_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Ronik_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")

    elif choice == 8:

        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Rahul_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Rahul_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Rahul_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")

    elif choice == 9:

        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Priyanshu_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Priyanshu_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Priyanshu_snacks.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("snacks details added sucessfully\n")

    elif choice == 10:

        details_type = int(
            input("Enter 1 to add food details\nEnter 2 to add chai/coffee\nEnter3 to add snacks\n"))
        if details_type == 1:
            data = input("Enter the food: ")
            with open("Bikash_food.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("Food details added sucessfully\n")

        elif details_type == 2:
            data = input("Enter the chai/coffee: ")
            with open("Bikash_chai_coffee.txt", 'a') as hk:
                hk.write(str([str(gettime())]) + " + " + data + "\n")
                print("chai/coffee details added sucessfully\n")

        elif details_type == 3:
            data = input("Enter the snacks: ")
            with open("Bikash_snacks.txt", 'a') as hk:
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

    elif choice == 4:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Mohak_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Mohak_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Mohak_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')

    elif choice == 5:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Prakash_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Prakash_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Prakash_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')

    elif choice == 6:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Nitish_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Nitish_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Nitish_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')
    elif choice == 7:
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
    elif choice == 8:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Rahul_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Rahul_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Rahul_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')

    elif choice == 9:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Ronik_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Ronik_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Ronik_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')

    elif choice == 10:
        details_type = int(
            input("Enter 1 to see details of Harry\nEnter 2 to see details of Mayank\nEnter3 to see details of Alok\n"))
        if details_type == 1:
            with open("Bikash_food.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 2:
            with open("Bikash_chai_coffee.txt") as hk:
                for data in hk:
                    print(data, end='')
        elif details_type == 3:
            with open("Bikash_snacks.txt") as hk:
                for data in hk:
                    print(data, end='')
    else:
        print("Enter a valid input\n")


print("\t\tWelcome to health management system")

add_see = int(input("Enter 1 to add details\nEnter 2 to see the details\n"))

if add_see == 1:
    usr_name = int(input(
        "Enter\n1 for Harry\n2 For Mayank\n3 for Alok\n4 for Mohak\n5 for Prakash\n6 for Nitish\n7 for Ronik\n8 for Rahul\n9 for Priyanshu\n10 for Bikash\n"))
    data_inp(usr_name)
else:
    usr_name = int(input(
        "Enter\n1 for Harry\n2 For Mayank\n3 for Alok\n4 for Mohak\n5 for Prakash\n6 for Nitish\n7 for Ronik\n8 for Rahul\n9 for Priyanshu\n10 for Bikash\n"))
    data_out(usr_name)
