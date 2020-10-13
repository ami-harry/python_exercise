# comprehension


'''
# make a list that have only numbers divisible  by 3
ls = []  # empty list

for i in range(100):
    if(i % 3 == 0):
        ls.append(i)

print(ls)

'''
'''

# making a list in a single line
# list comprehension
ls = [i for i in range(100)]
ls1 = [i for i in range(100) if i % 3 == 0]
print(ls)
print(ls1)

'''


# dictiornary comprehension
# set comprehension
# generator comprehension

# dictionary comprehension
# dict1 = {i: f"Item{i}" for i in range(10)}
# dict2 = {i: f"Item{i}" for i in range(100) if i % 5 == 0}
# print(dict1)
# reverse of the dict1 #the key will become value and value will become key
# dict1 = {value: key for key, value in dict1.items()}
# print(dict1)
# print(dict2)


# set comprehension
'''
dresses = {dress for dress in ["dress1", "dress2",
                               "dress3", "dress2",
                               "dress4", "dress1",
                               "dress2", "dress3"]}
print(dresses)
print(type(dresses))


'''
'''


# generator comprehension

evens = (i for i in range(20) if i % 2 == 0)
print(type(evens))

print(evens)
print(id(evens))

for i in evens:
    print(i)

'''
