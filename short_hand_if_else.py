# short_hand if else or one liner statement


a = int(input("Enter a: "))
b = int(input("Enter b: "))


'''
# normal way
if (a > b):
    print("A is greater than B")
else:
    print("B is greater than A")
'''

# one liner statement
print("B is greater than A") if(a < b) else print("A is greater than B")
