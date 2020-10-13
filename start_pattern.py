'''
# printing star

print("pattern printing")
num = int(input("Enter how many rows you want to print\n"))
print("Enter 0 or 1")
bool_val = input("Enter 1 for true and 0 for false\n")
if bool_val == "1":
    for i in range(1, num+1):
        print("*"*i)
if bool_val == "0":
    for i in range(num, 0, -1):
        print("*"*i)


'''

print("Patter printing")

rows = int(input("Enter how many rows you want to print\n"))
bool_num = input("Enter 1 to print increasing order and 0 for decreasing")
if bool_num == "1":
    for i in range(1, rows+1):
        print("*"*i)

if bool_num == "0":
    for i in range(rows, 0, -1):
        print("*"*i)
