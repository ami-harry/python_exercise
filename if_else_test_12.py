# take input the age and check these conditions
# if age is greater than 18 you can drive, if equal to 18 , we cannt decide and if less that 18 then you cann't drive

age = int(input("Enter your age: "))

if age > 100:
    print("Enter age in limit")
elif age == 18:
    print("We can't decide, come to office we will decide ")
elif age > 18:
    print("You can drive !!")
else:
    print("oops, you can't drive")
