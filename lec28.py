 #exercise 4

 # pattern printing
#  1 for increasing order
#  0 for decreasing
#  input n rows



row=int(input("Eneter how many rows you want to print"))
bool_val=int(input("Enter 1 for true and 0 for false"))

bool(bool_val)
if bool_val==1:
    for i in range(0,row+1):
        print("*")
elif bool_val==0:
    for i in range(row+1, 1):
        print("*")
else:
    print("Enter valid input")