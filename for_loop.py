# accessing the elements of list and dict

list1 = [['harry', 21], ['rahul', 58], ['priyanshu', 54], ['hariom', 34]]
# this is an list of list

# accessing its data

print("Data of list using for loop")
for data in list1:
    print(data)

# it will give the output as a list
print()

# here we are printing all the items
for name, roll in list1:
    print("you name is", name, "and roll no is", roll)
print()


# typecasting the same list into a dict
#  and accessing the items of that dict
dict1 = dict(list1)

print("Data of dict using for loop")
for name in dict1:
    print(name)
print()
# it will give all the keys value
#  to access its key value pair we have to use dict.items for that
# it will return all the keys and value for all the items

for name, roll in dict1.items():
    print("you name is", name, "and roll no is", roll)
print()

# printing all keys
print("all keys are")
key = dict1.keys()
print(key)  # it will return all the keys in a list form
print()
print("printing all values")
val = dict1.values()
print(val)


# printing data using condition
for name, roll in dict1.items():
    if rry in name:
        print(name, roll)
