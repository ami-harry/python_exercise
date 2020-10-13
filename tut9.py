# list
'''
a1 = ["hii", "hello", 54, 34, 78.56]
print(a1)
print(type(a1))
print(a1[2])
print(a1[4])
print(a1[1:4])
print(a1[4:1])
print(a1[::-1])
print()


a = [34, 23, 67, 32, 43, 1, 54]
print(a)
print(type(a))
print(a[4])
print(a[2])
print(a[2:5])
print(a[::-1])
print(a[2:5:2])
a.sort()
print(a)
a.reverse()
print(a)
print()
print()
ret_list = a[2::2]
print(ret_list)

print(len(ret_list))
print(max(a))
print(min(a))


a2 = [34, 23, 67, 32, 43, 1, 54]
print(a2)
a2.append("harry")
a2.append("hello")
a2.append(5)
print(a2)

# append method adds a element at the end of the list
# insert-- this method is used to insert an element at specific position
a2.insert(3, "3rd index")
print(a2)
# remove()--> it will remove the give no
# pop()--> this will delete the last element of the list
a2.pop()
print(a2)

a3 = [34, 23, 67, 32, 43, 1, 54]
print(a3)
a3[4]="changed"
print(a3)
# we can change the value of list, this is mutable

'''

# tuple
# we cant change the value of tuple, this is immutable
# a1 = (1, 4, 2, 6, 34)
# print(a1)
# print(type(a1))
# a1[2] = "changed"  # this will give error, we cant change the value
# if the tuple has only one element , we have to give comma after the element
# a = (10) #This is invalid tuple
# a = (10,) #This is valid tuple

# swapping the values
# a, b = 10, 15
# print(a, b)
# a, b = b, a
# print(a, b)
# done, swapping done

print("hello this is running in pycharm")

a11=int(input("Enter the number"))
print(a11+10)