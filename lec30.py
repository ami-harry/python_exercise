# opening the file using with() mode
# in this mode , we need not to close the file

# with block
with open("harry1.txt") as fp: #opening the file as fp
    # print(fp.readline())# reading a line
    a=fp.read(10)# reading 10 character and storing it into a variable
    print(a)