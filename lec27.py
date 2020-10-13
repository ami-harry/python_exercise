# writing  and appending into the file

# f=open("harry2.txt","w") #if the file is not present, it will create, if the file is present, the old content will be replaced
# f.write(" harry bhai bht achhe hai ")
# print('file writing done')
# f.close()
#
# print('reading the file')
# f=open("harry2.txt")
# print("file opened for reading")
# print(f.readlines())
# f.close()


# to check how many character we have write into the file

# f=open("harry2.txt","w") #if the file is not present, it will create, if the file is present, the old content will be replaced
# a=f.write(" harry bhai bht achhe hai ")# a will strore the no of character written in the file
# print('file writing done')
# print(a)
# f.close()
#

# opening the file for reading and writing
f=open("harry2.txt","r+")
print(f.read())
f.write(" thanks ") #writing into the file
print(f.read())
f.close()

