
# IO basics operations

'''
# 'r' --> open a file for reading (default)
# 'w' --> open a file for writing
# 'x' --> creates a new file if name doesn't exists
# 'a' --> add more context at the end of the file
# 't' --> text mode (default)
# 'b' --> binary mode
# '+' --> read and write

'''
'''

# here we are making an opening a text file using open().
# open() returns a file pointer
#

f = open('harry.txt')
# in open function we can pass more IO methods as, r,rt,rb,a and all
# rt mode is by default
# here read function will return all the content of the file into data variable


# data = f.read()
# we can print the data variable and we can see what is insite the harry.txt file
# print(data)

# we can read the data as per our choice,,we can read the data using char length..how many characters we want to see

data1 = f.read(7)  # it will read 7 characters
print(data1)

data1 = f.read(7)  # it will read next 7 characters including spaces
print(data1)

f.close()  # we must close the file which was opened

'''

# printing the file data using line by line

f = open("harry.txt")

# this will return a single line...as much we write this statement it will return the next lines
# print(f.readline())
# readline() -> this will print a single line

# if we use readlines() --> this will return all the lines in form of list including \n
print(f.readlines())


# printing the line by line using iteration

for line in f:
    print(line, end='')  # this will print all the lines of the file
