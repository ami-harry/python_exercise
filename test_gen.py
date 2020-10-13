# make a generator
# find the factorial no generator by generator


def no_gen(n):
    for i in range(n):
        yield i


num = no_gen(10)
'''
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
'''

'''
for n in num:
    print(n)
'''


def fact(num):
    for i in num:
        return i*fact(i-1)


print(fact(num))
