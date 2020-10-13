# os module
import os

'''
# what operations we can do with os module, we can se by dir.os
# print(dir(os), end='\n')
a = dir(os)
for data in a:
    print(data, end='\n')
'''

'''
# working directory

print(os.getcwd()) #it will return the current working directory
a = os.getcwd() #it will return the current working directory
print(a)

'''
'''

# changing the working directory
a = os.getcwd()  # it will return the current working directory
print(a)
os.chdir("/home/hariom/Desktop")
print(os.getcwd())

# after changing the directory if we want to access the file of previous directory, it will give error
'''
'''


# to see all the files of current directory
# print(os.listdir())
# print(os.listdir("/home/hariom/Desktop"))

'''
'''

# making a folder

os.mkdir("harry")  # ye folder bn jayega
print("folder created")

# if we want to make folder inside folder and the main folder is not available , it will create a main folder then after it will create a folder inside that folder
os.makedirs("harry/hariom/hk")  # this will make folder inside folder
print("folder inside folder created\n")

'''
'''

# renaing a foler/file
os.rename("harry", "new_name")
print("folder name changed")
'''
'''

# getting enviornment variables

print(os.environ.get('Path'))

'''
'''

# os.join
print(os.path.join("/home/hariom/Desktop", "harry1.txt"))
'''
'''

# checking that the path  exists or not
# it will return True or False

print(os.path.exists("/home/hariom/Desktop"))
print(os.path.exists("/home/hariom/Desktop/hk"))

'''
'''

# checking the type of path
print(os.path.isfile("/home/hariom/Desktop"))
print(os.path.isdir("/home/hariom/Desktop"))

'''
