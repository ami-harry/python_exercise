# enumerate function

#
'''

l1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


# printing only odd index elements
i = 1
for item in l1:
    # if i % 2 is not 0:
    if i % 2 != 0:
        print(f"this is odd--> {item}")
    i += 1

'''
# to make this function easier, in python , we have enumurated function


l1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# enumerate function returns index and value so that we cant perform the same task in easier way
for index, item in enumerate(l1):
    if index % 2 is 0:
        print(f"this is odd--> {item}")
