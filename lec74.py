# using else with for loop

khana = ['vat', 'dal', 'roti', 'sbji']

''' 

for food in khana:
    print(food)
    # break if we use break statement then the else block will not run
else:
    print("The for loop executed properly")

'''

for item in khana:
    if item == 'kachori':
        print(item)
        break
#         if the conditions fails then else block will execute
else:
    print("your item was not found in for loop")
