# freading file (r/rt)

# to write in the file, we have to open that file, to open the filem we have to make a file pointer and that will help to write inside the file
# f is the file pointer


# reading the file, without giving any mode, becuase r mode is default
# f=open("harry1.txt")
# content=f.read() #storing the data of file into ontent variable
# print(content)
# f.close() #closing the file

# f=open("harry1.txt","r")
# f=open("harry1.txt","rt")
# content=f.read() #storing the data of file into ontent variable

# reading limited character
# content=f.read(5) # it will read first 5 character
# print(content)
# f.close() #closing the file


# reading the file line by line
# f=open("harry1.txt")
# for line in f:
#     print(line,end=' ')
# f.close()



# readline function
# f=open("harry1.txt")
# print(f.readline()) #this will print first line
# print(f.readline()) #this will print second line
# f.close()

# reading multiple lines
# f=open("harry1.txt")
# print(f.readlines()) #this will print all the lines in a list
# f.close()