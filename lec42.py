# time module

'''
# finding the execution time of a program
import time

initial1 = time.time()  # time time.time() method gives a tick
print(initial1)

for i in range(50):
    print("this is harry")
print("for loop runs in ", time.time()-initial1, " seconds")

# print("for loop end")
print()


initial2 = time.time()  # time time.time() method gives a tick
print(initial2)
k = 0
while k <= 50:
    print("this is harry")
    k = k+1
print("for loop runs in ", time.time()-initial2, " seconds")
print("while loop end")

'''
import time

# this will give current time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# time.sleep() # it holds the program for given time

i = 0
while i < 10:
    print(localtime)
    time.sleep(2)
    i += 1
