# break and continue
# break statement is used to break the loop
# continue means to escape that occurnce

# i =0
# while (i<45):
#     print(i,end=" ")
#     i+=1
#


# i=0
# while True:#this is infinite loop
#     print(i,end=' ')
#     i+=1

# i=0
# while True:
#     print(i,end=' ')
#     if(i==50):
#         break #the program will break at 50
#     i+=1

"""


i=0
while True:
    if i+1<5:
        i+=1
        continue #the loop will escape i till less than 5
    print(i,end=' ')
    if(i==50):
        break #the program will break at 50
    i+=1
"""


# quiz
# take input untill the user gives input >100

while True:
    inp=int(input("Enter a number: "))
    if(inp<100):
        print("Oops try again !")
        continue
    else:
        print("Congrats you have entered number greater than 100")
        break