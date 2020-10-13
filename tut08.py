# strings and string operations


h1 = "hello this is a string"
print(h1)

# slicing on string
# print(h1[index])
# print(h1[start:end:step])

# print(h1[:5]) #this will print 0 to 4
# this will give the length of the string. so that we can slice the staring. from 0 to 18
# print(len(h1))
# print(h1[55])  # this will give error if the index size is out of range
# print(h1[0:55])  # this will give the full string if the end is out of range


# more on slicing
# print(h1[0:50:2])
# print(h1[::2])  # means 0 to all will step size 2
# print(h1[0::2])  # means 0 to all will step size 2
# print(h1[:10:2])  # means 0 to 9 and  with step size 2
# print(h1[::])  # means 0 to all with step size 1

# -ve index

# print(h1[-1:])  # this will print from last
# print(h1[-5:])  # this will print 4 char from last
# print(h1[-10:-7])  # this will print from last
# print(h1[::-1])  # this will reverse the string
# print(h1[-2:-5:-1])  # this will reverse the string


# functions of string

print(type(h1))
# print(h1.isalnum())  # if the string has spaces then it will be false, (alphanumeric)
# b = "thisisng"
# print(b.isalnum())  # this will give true becuase the string has no spaces
# print(h1.isalpha())
# print(h1.endswith("string"))  #it will return as per condition
# print(h1.count("s"))  # it will return how many times 's' in the string
# print(h1.capitalize())  # this will captalize the first letter of the string
# print(h1.find("is"))  # this will tell at which index the string is present at
# print(h1.upper())
# print(h1.lower())
# print(h1.replace("is", "this is replaced"))
