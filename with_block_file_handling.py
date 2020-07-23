# f = open("file_writing.txt")
#
# print(f.readline())  # this will give a single line
# print(f.readlines())  # this will give all lines in form of list
# f.close()

# using with block
# using with block we dont need to close the file
# with open("filename ") as var: -->syntax


with open("file_writing.txt", 'r+') as hk:
    # all_lines = hk.readlines()
    # print(all_lines)
    # single_line = hk.readline()
    # print(single_line)






    # printing using char no
    # no_of_char = int(input("Enter how many char you want to print: "))
    # a = hk.read(no_of_char)
    # print(a)





    '''
    # r+ used to writng more data in the file
    hk.write("\n hey this line was added using r+ in with mode")
    line = hk.readlines()
    for lines in line:
        print(lines, end='')
    print()
    '''
