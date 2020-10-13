# lambda or anonymous function(unnamed function)
# function without name

# normal function
# def add(a,b):
#     return a+b

# lambda function

# sum = lambda x, y:x+y #this is one liner function
# print(sum(5,3))


# def a_first(a):
#     return a[1]
#     return a[0]


# a = [[1, 14], [15, 66], [8, 1]]  # list of list
# # print(a)
# a.sort(key=a_first)
# print(a)


a = [[1, 14], [15, 66], [8, 1]]  # list of list
print(a)
a.sort(key=lambda x: x[0])
# a.sort(key=lambda x: x[1])
print(a)
