# coroutines
# it is used when some function is taking some time to start, the fucntion is started once, it will run faster for next inputs
def searcher():
    import time
    print("reading a book and consuming 4 seconds")
    book = "this is a book on gitm and gitm is a college in hariyana gurugram, harry"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print(f"Your text {text} is in the book")
        else:
            print(f"Text {text} is not in the book")


s = searcher()
print("search started")
next(s)  # this is coroutines
s.send("harry")  # sending the input to find the text in the function
s.close()  # this will close the searcher

# if we try to send after closing the coroutine it will give an error
# s.send("hii")  # this will give error, because s is already closed
'''

input("press any key key")
s.send("h")
input("press any key")
s.send("ok")
input("press any key")
s.send("hii")
input("press any key")
s.send("gitm")
'''
