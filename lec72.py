# generators in python

# iterator/iterable/iteration
'''

iterable--> __iter__() or __getitem__()
iterator--> __next__()
iteration-->

'''

'''

for i in range(78):
    print(i)

'''


def gen(n):
    for i in range(n):
        yield i  # it will generate the value


# g = gen(10000)
# print(g)  # this is a generator

# generators are used

# make two programs
# fibonacii and factorial
# using generator
# gerators can be iterate only once


g = gen(5)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# if limit exceed it will show error

# for i in g:
#     print(i)


'''
h = "harry"  # string is iterable

# using iterators method
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())


# using iterative method
# for char in h:
#     print(char)
#

'''


