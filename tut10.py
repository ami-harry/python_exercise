# dictonary
# dictonary is nothing but key value pair


d1={}
print(type(d1))

d2={"harry":"hk",5:10,"shalini":"keshav"}
print(d2)


# print(d2["harry"])#accessing an value using key
# updating / adding elements in the dict
d2["aptech"]="sitamarhi" #this will be added in the last
# print(d2)

# deleting an key-value from dict
# del d2[5]
# print(d2)
# print(d2["shalini"])

# copying dict
# d3=d2 #dict d2 is been copied to d3
# print("d2 is",d2)
# print("d3 is",d3)

# if we made changes in d3 it will effecr d2, becuase using this method d3 and d2 will allocate both dict, so the chages will effect on both of them

# using .copy function

# d3=d2.copy()#this means a copy of d2 has been given to d3, both have now different addess, so changes will not effect to each other
# print("d2 is",d2)
# print("d3 is",d3)
#
# del(d3["harry"])
# print("d2 is",d2)
# print("d3 is",d3)
# d2.update("svm":"school")
# print(d2.keys()) #this will print all the keys of the dict
# print(d2.items()) #this will print all the dict key value in form of tuple
