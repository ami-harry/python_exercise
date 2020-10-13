# else and finally in try except
# try except else finally
from logging import exception

'''
try:
    f = open("haary.txt")
except Exception as e:
    print(e)  # the error will be printed as string
print("important lines")

'''
'''
f1 = open("harry1.txt")
try:
    f = open("harry2.txt")  # this file also exists
except Exception as e:
    print(e)  # the error will be printed as string
finally:
    print("run this line anyway")
    print("run this line anyway")
    f.close()
    f1.close()
print("important lines")
'''

# finally will be run , no matter exception was happened or not(finally is used for code cleanup)
# else will run when except will not run, if except will run then else will not run


'''

f1 = open("harry1.txt")
try:
    f = open("har.txt")
# except Exception as e:
    print(e)  # the error will be printed as string
else:
    print("this will run only if except is not running")
finally:
    print("run this line anyway")
    print("run this line anyway")
    # f.close()
    f1.close()
print("important lines")
# finally will run no matter try or except is running
'''

# if we have  more than one error, handling more than one error
f1 = open("harry1.txt")
try:
    f = open("har.txt")
except OSError as e:
    print("OS error aa gya hai bhai")
except Exception as e:
    print(e)  # the error will be printed as string
except EOFError as e:
    print("eof error aa gya hai bhai")
except IOError as e:
    print("IO error aa gya hai bhai")
else:
    print("this will run only if except is not running")
finally:
    print("run this line anyway")
    print("this is finally block")
    print("run this line anyway")
    # f.close()
    f1.close()

print("important lines after try except else finally block")
