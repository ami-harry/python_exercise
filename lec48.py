# map(), filter(), reduce() functions

# l1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# l2 = ["1", "2", "3", "4", "5", "6"]
# changing all the strings into integer
# for item in range(len(l2)):
#     l2[item] = int(l2[item])

# print(l2[3])
# print(l2[3]+10)
# running for loop everytime is not good, so we will use map() function


# map() function
# l2 = ["1", "2", "3", "4", "5", "6"]
# typecasting the items into int and storing it into a list
# l3 = list(map(int, l2))
# print(l2)
# print(type(l2))
# print(type(l2[3]))
# print(l3)
# print(type(l3))
# print(type(l3[3]))


# def sq(a):
#     return a*a


# num = [3, 2, 5, 7, 3, 8]
# square = list(map(sq, num))
# print(num)
# print(square)


# using lambda function with map
# num = [3, 2, 5, 7, 3, 8]
# square = list(map(lambda x: x*x, num))
# print(num)
# print(square)

'''
def sq(a):
    return a*a


def cube(a):
    return a*a*a


# num = [3, 2, 5, 7, 3, 8]
funs = [sq, cube]
for i in range(5):
    val1 = list(map(lambda x: x(i), funs))
    print(val1)

'''

'''
# filter() function
# it returns true if the function condition satisfies


num = [3, 2, 5, 7, 3, 8]


def is_greater(num):
    return num > 5


greater_than_5 = list(filter(is_greater, num))
print(greater_than_5)
# filter returns a list, we need to typecast it into list

'''


# reduce()
# finding sum using iterative method
# list1 = [3, 2, 5, 7, 3, 8, 12]
# num = 0
# for i in list1:
#     num = num + i
# print(num)


'''
from functools import reduce
num = [3, 2, 5, 7, 3, 8, 12]
prod = reduce(lambda x, y: x+y, num)
print(prod)

'''

# from functools import reduce
# num = [3, 2, 5, 7, 3, 8, 12]
# sq = reduce(lambda x, y: x*y, num)
# print(sq)
