 # file I/O operations


# "r"---> read mode--> open file for reading , it is default mode
# "w"--> writing mode--> open file for writing, it will create the file if doesn't exists and will erase previous data if the file has.
# "x"--> file the file exists, it will fail, if file is not present it will create a file
# "a"-->append--> this will add the text in the last of the file, if file doesn't exists, it will create
# "t"-->text mode--> it means our file is a text file...opening the file in text mode, it is default mode
# "b"-->bihary mode-->it  means file is in binary mode
# "+"--> read and write



# quiz-->
# how to print the doc-string of the function
def my_fun():
    """this is doc-string
    this funcion take nothing and returns nothing"""
    print("function is calling")

my_fun()
print(my_fun.__doc__)