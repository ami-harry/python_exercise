import datetime


def gettime():
    return datetime.datetime.now()


def topic_add(sub_name):
    if sub_name == 1:
        topic = int(input(
            "Enter\n1 to add learned topics\n2 to add important topics\n3 to add remaining topcs\n4 to add projects name\n"))

        if topic == 1:
            data = input("Enter data: \n")
            with open("python_new_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + " --> " + data + "\n")
                print("Python learned topics has been added sucessfully\n")

        elif topic == 2:
            data = input("Enter data: \n")
            with open("python_imp_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("Python important topics has been added sucessfully\n")

        elif topic == 3:
            data = input("Enter data: \n")
            with open("python_rem_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("Python remaining topics has been added sucessfully\n")

        elif topic == 4:
            data = input("Enter data: \n")
            with open("python_projects.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("Python projects topics has been added sucessfully\n")
        else:
            print("enter valid input\n")
            print()

    elif sub_name == 2:
        topic = int(input(
            "Enter\n1 to add learned topics\n2 to add important topics\n3 to add remaining topcs\n4 to add projects name\n"))

        if topic == 1:
            data = input("Enter data: \n")
            with open("java_new_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("java learned topics has been added sucessfully\n")

        elif topic == 2:

            data = input("Enter data: \n")
            with open("java_imp_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("java important topics has been added sucessfully\n")

        elif topic == 3:
            data = input("Enter data: \n")
            with open("java_rem_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("java remaining topics has been added sucessfully\n")

        elif topic == 4:
            data = input("Enter data: \n")
            with open("java_projects.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("java projects topics has been added sucessfully\n")
        else:
            print("Enter valid input\n")
            print()

    elif sub_name == 3:
        topic = int(input(
            "Enter\n1 to add learned topics\n2 to add important topics\n3 to add remaining topcs\n4 to add projects name\n"))

        if topic == 1:
            data = input("Enter data: \n")
            with open("c++_new_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("c++ learned topics has been added sucessfully\n")

        elif topic == 2:
            data = input("Enter data: \n")
            with open("c++_imp_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("c++ important topics has been added sucessfully\n")

        elif topic == 3:
            data = input("Enter data:\n ")
            with open("c++_rem_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("c++ remaining topics has been added sucessfully \n")

        elif topic == 4:
            data = input("Enter data: \n")
            with open("c++_projects.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("c++ projects topics has been added sucessfully\n")
        else:
            print("Enter valid input\n")
            print()

    elif sub_name == 4:
        topic = int(input(
            "Enter\n1 to add learned topics\n2 to add important topics\n3 to add remaining topcs\n4 to add projects name\n"))

        if topic == 1:
            data = input("Enter data: \n")
            with open("c_new_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("c learned topics has been added sucessfully\n")

        elif topic == 2:
            data = input("Enter data: \n")
            with open("c_imp_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("c important topics has been added sucessfully\n")

        elif topic == 3:
            data = input("Enter data:\n ")
            with open("c_rem_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("c remaining topics has been added sucessfully\n")

        elif topic == 4:
            data = input("Enter data:\n ")
            with open("c_projects.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("c prokects topics has been added sucessfully\n")
        else:
            print("Enter valid input\n")
            print()

    elif sub_name == 5:
        topic = int(input(
            "Enter\n1 to add learned topics\n2 to add important topics\n3 to add remaining topcs\n4 to add projects name\n"))

        if topic == 1:
            data = input("Enter data:\n ")
            with open("WEB_new_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("WEB learned topics has been added sucessfully\n")

        elif topic == 2:
            data = input("Enter data:\n ")
            with open("WEB_imp_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("WEB important topics has been added sucessfully\n")

        elif topic == 3:
            data = input("Enter data:\n ")
            with open("WEB_rem_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("WEB remaining topics has been added sucessfully\n")

        elif topic == 4:
            data = input("Enter data:\n ")
            with open("WEB_projects.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("WEB projects topics has been added sucessfully\n")
        else:
            print("Enter valid input\n")
            print()

    elif sub_name == 6:
        topic = int(input(
            "Enter\n1 to add learned topics\n2 to add important topics\n3 to add remaining topcs\n4 to add projects name\n"))

        if topic == 1:
            data = input("Enter data:\n ")
            with open("java_script_new_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("java_script learned topics has been added sucessfully\n")

        elif topic == 2:
            data = input("Enter data: \n")
            with open("java_script_imp_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("java_script important topics has been added sucessfully\n")

        elif topic == 3:
            data = input("Enter data:\n ")
            with open("java_script_rem_topic_add.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("java_script remnaining topics has been added sucessfully\n")

        elif topic == 4:
            data = input("Enter data:\n ")
            with open("java_script_projects.txt", "a") as hk:
                hk.write(str([str(gettime())]) + "-->" + data + "\n")
                print("java_script projects topics has been added sucessfully\n")
        else:
            print("Enter valid input\n")
            print()
    else:
        print("Enter a valid input\n")
        print()


def topic_see(sub_name):
    if sub_name == 1:
        topic = int(input(
            "Enter\n1 to see learned topics\n2 to see important topics\n3 to see remaining topcs\n4 to see projects name"))

        if topic == 1:
            with open("python_new_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 2:
            with open("python_imp_topic_add.txt", "a") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 3:
            with open("python_rem_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 4:
            with open("python_projects.txt") as hk:
                for data in hk:
                    print(data)
                print()
        else:
            print("enter valid input")
            print()

    elif sub_name == 2:
        topic = int(input(
            "Enter\n1 to see learned topics\n2 to see important topics\n3 to see remaining topcs\n4 to see projects name"))

        if topic == 1:
            with open("java_new_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 2:
            with open("java_imp_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 3:
            with open("java_rem_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 4:
            with open("java_projects.txt") as hk:
                for data in hk:
                    print(data)
                print()
        else:
            print("Enter valid input")
            print()

    elif sub_name == 3:
        topic = int(input(
            "Enter\n1 to see learned topics\n2 to see important topics\n3 to see remaining topcs\n4 to see projects name"))

        if topic == 1:
            with open("c++_new_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 2:
            with open("c++_imp_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 3:
            with open("c++_rem_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 4:
            with open("c++_projects.txt") as hk:
                for data in hk:
                    print(data)
                print()
        else:
            print("Enter valid input")
            print()

    elif sub_name == 4:
        topic = int(input(
            "Enter\n1 to see learned topics\n2 to see important topics\n3 to see remaining topcs\n4 to see projects name"))

        if topic == 1:
            with open("c_new_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 2:
            with open("c_imp_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 3:
            with open("c_rem_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 4:
            with open("c_projects.txt") as hk:
                for data in hk:
                    print(data)
                print()
        else:
            print("Enter valid input")
            print()

    elif sub_name == 5:
        topic = int(input(
            "Enter\n1 to see learned topics\n2 to see important topics\n3 to see remaining topcs\n4 to see projects name"))

        if topic == 1:
            with open("WEB_new_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 2:
            with open("WEB_imp_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 3:
            with open("WEB_rem_topic_add.txt", "a") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 4:
            with open("WEB_projects.txt", "a") as hk:
                for data in hk:
                    print(data)
                print()
        else:
            print("Enter valid input")
            print()

    elif sub_name == 6:
        topic = int(input(
            "Enter\n1 to see learned topics\n2 to see important topics\n3 to see remaining topcs\n4 to see projects name"))

        if topic == 1:
            with open("java_script_new_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 2:
            with open("java_script_imp_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 3:
            with open("java_script_rem_topic_add.txt") as hk:
                for data in hk:
                    print(data)
                print()

        elif topic == 4:
            with open("java_script_projects.txt") as hk:
                for data in hk:
                    print(data)
                print()
        else:
            print("Enter valid input\n")
            print()
    else:
        print("Enter a valid input\n")
        print()

print("\t\t\t\t\t\tHarry")
print("\t\t\t\t Welcome to skill tracking records program\t\t\t\n")

choice = int(input("Enter\n1 to add\n2 to see the details:\n "))

if choice == 1:
    lang_name = int(input(
        "Enter\n1 for Python\n2 for Java\n3 for c++\n4 for c\n5 for WEB\n6 for java script\n"))
    topic_add(lang_name)

elif choice == 2:
    lang_name = int(input(
        "Enter\n1 for Python\n2 for Java\n3 for c++\n4 for c\n5 for WEB\n6 for java script\n"))
    topic_see(lang_name)

else:
    print("Enter valid input\n")
print("Thanks for using this progra")