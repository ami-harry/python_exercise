# make a coroutine
# make a list of 15 students and ask the user for input and tell him that his name is in the list or not

def search_name():
    from time import sleep
    name = ["harry", "mohak", "nitish", "ronik", "priyanshu", "rahul", "ronik", "alok", "mayank", "pandey", "vivek",
            "raju", "ajay", "hariom", "shalini", "keshav"]
    print("reading the names")
    sleep(4)

    while True:
        n = yield
        print(f"Your name {n} is in the name list")
    else:
        print(f"Your name {n} is not in the name list")


h = search_name()
data = input("Enter name to search")
next(h)
h.send(data)

