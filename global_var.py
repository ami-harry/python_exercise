
'''

glob = 20


def fun(n):
    n = 10
    print(n, "hello mai print ho gya")
    print(glob)


fun(20)
# print(n) hre it will give error , becuase n is a local variable
print(glob) 

# we cant modify global varible inside the function
#  if inside the function the variable name is same  for local and global
# local will given more value , it will access and can be modified
# to access the global variable and modify that value we have to use global key word following with variable name to access it and modify the value globally




'''


x = 50  # global


def harry():
    x = 20  # local var for function harry

    def hariom():  # this is nested function
        global x
        x = x+100  # modifing the global x
        print("after modifyng the x inside the hariom function")
        print('x is ', x)
        print()
    print("before calling the hariom function x is ", x)
    hariom()
    # it will give 20 becuase for function harry x is local variable
    print("after calling the hariom function x is ", x)


harry()
print()
print("printing the global variable outside the function")
print(x)
