f = open("file_writing.txt")

# tell() it tells that where is out file pointer. it will return the character no


# to reset the file pointer at a specific poition we use seek function


print(f.tell())
print(f.readline())

# here the tell function is showing that th file pointer is at a specifi char location
print(f.tell())
# using seek function we can change the position of the file pointer and we from now the file pointer will print data from that point
print(f.readline())

f.seek(10)  # it will print form 10th char
# we can give input
print(f.tell())
print(f.readline())

# print(f.tell())

print(f.tell())
print(f.readline())
char_no = int(input("Enter the char location form where you want to print "))
f.seek(char_no)
print(f.tell())
print(f.readline())

f.close()
