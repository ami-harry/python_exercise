# loops in python

# lst=["harry","raju","vivek","ranjeet","arvind","shekhar"]
# print(lst)

# for item in lst:
    # print(item)
# lst=[["harry",1],["raju",4],
#      ["vivek",44],["ranjeet",77],
#      ["arvind",55],["shekhar",45]]
# #this is list of list
#
# for name , roll in lst:
#     print(name, " and roll is "       , roll   )
#
# lst2=[["harry",1],["raju",4],
#      ["vivek",44],["ranjeet",77],
#      ["arvind",55],["shekhar",45]]

# typecasting this list of list to dict
# we cant access dict elemenets directly, we have to use dict.items() then after we can access it
# print(type(lst2))
# dic=dict(lst2)
# print(type(dic))
'''
for name , roll in dic:
    print(name, " and roll is "       , roll   )
we cant access directly

'''

# for name , roll in dic.items():
#     print(name, " and roll is ", roll)

#



# quiz
# make a list and print the item if the number is greater than 6
"""


lst=[1,65,3,78,4,67,4,67,23,6,2,8,12,86,34]
print("the original list is")
print(lst)
print()
print("the filtered number greater than 6 with sorted manner")
lst.sort()
for item in lst:
    if item>6:
        print(item)
"""


# quiz 1
# make a list and print those items which are ends with y
name=["harry","marie","cary","lary","hope","hii",'hello',"ok","okay","achaa"]
print(("the original list is"))
print(name)
for data in name:
    if name.data  with 'y':
        print(data)