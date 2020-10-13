# write and append


#initially our file pointer is at 0, so f.tell will print 0
f=open("harry1.txt") #opening the file in default mode
print(f.tell()) #this will tell that where is out file pointer
print(f.readline())
print(f.tell()) #this will tell that where is out file pointer
print(f.readline())
f.seek(5) #this will reset the file pointer to the value passed, this will take file pointer to 5
print(f.tell()) #this will tell that where is out file pointer
print(f.readline())
print(f.tell()) #this will tell that where is out file pointer
f.seek(0) #this will reset the file pointer to the value passed, this will take file pointer to 5
print(f.readline())
print(f.tell()) #this will tell that where is out file pointer
f.close()