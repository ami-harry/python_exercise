# args and coargs

# def fun1(a, b, c, d, e):
#     print(a, b, c, d, e)


# fun1("harry", "hk", "mohak", "ronik", "nitish")
# what if we have infinite no of users?
# we will use will use *args concept


'''
def fun2(normal, *args):
    print(normal)
    print(type(args))  # it accepts input as tuple
    # print(args[0]) #it will give 0th index name
    for i in args:
        print(i)


normal = "this is normal argument"
har = ["harry", "hk", "mohak", "ronik", "nitish"]
# fun2(*har)
fun2(normal, *har)

# order of arguments,
normal, args, coargs

'''
'''


def fun3(*val):
    print(type(val))
    for data in val:
        print(val)


# har = ["harry", "hk", "mohak", "ronik", "nitish"]
# fun3(har)

'''
'''


def fun4(normal, *args, **kwargs):  # **kwargs take input as dict,(key-value pair)
    print(normal)
    print(type(args))
    print(type(kwargs))
    for data in args:
        print(data)
    for i in kwargs:
        print(i)


har = ["harry", "hk", "mohak", "ronik", "nitish"]
n = "this is normal"
har1 = ["harry1", "1hk", "m11oh1ak", "ro1n11ik", "ni1111tish"]
fun4(n, *har, **har1)

'''
'''


def fun5(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(f"{key} is a value  {value}")


normal = "this is normal"
har = ["harry", "hk", "mohak", "ronik", "nitish"]
kw = {"harry": "programmer", "he": "she", "ok": "thik hai", "ha": "hmm"}
fun5(normal, *har, **kw)

'''