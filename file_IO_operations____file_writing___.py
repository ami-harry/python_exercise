'''
# creating a file and opening it in write mode

# f = open("file_writing.txt", "w")

# if the file name exists the previous data will be replaced
# if file name doesn't exists it will create a new one


# f.write("hello we are writing this into the file")
# using file pointer.write we can add data to the file

# everytime when we run this program, it will create a new file and the data will be replaced

# f.close()  # here we are closing the file which we have openend


# opening the file in append mode

# to add the data in existing file we have to open the file in append mode
# append mode will not replace old content of the file

app_file = open("file_writing.txt", "a")
read_file = open("file_writing.txt", "r")

# this data will be added to the next line of the file
data_write = app_file.write(
    "\nhey, this value is appending to the existing file\n")

# to check how many character we have added in the file
print(data_write)


# reading the lines of the file

print(read_file.readline())

app_file.close()
read_file.close()
'''


# to perform read and write (r+)


f = open("file_writing.txt", 'r+')

print(f.read())
# this will return all content of the file

# if we want to add something in the file
f.write("thanks")  # this will be added in the last
print(f.read())

f.close()
