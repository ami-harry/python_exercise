# exercise 3
# guess the number

# take input from user and match with your number
# if the number is greater say him
# if the number is less say him
# if matches, say wow
# no of guesses =10
# print after every try, no of guess left
# if guesses are over then print game over

num=49
no_of_guesses=1
print("\t\t\t\t\tWelcome to no guessing quiz")
print("No of guesses are limited ti 10")
while no_of_guesses<11:
    user_inp=int(input("Enter your number: "))
    if user_inp>num:
        print("You have entered a greater number than original ")
    elif user_inp<num:
        print("You have entered a smaller number than original")
    else:
        print("you won")
        print("you took ",no_of_guesses," inputs to guess the correct input")
        print(10-no_of_guesses, " inputs are left to guess the number")
        break
    print(10-no_of_guesses, " inputs are left to guess the number")
    no_of_guesses+=1
if no_of_guesses>10:
    print("game over")
    print("0 chances  are left")

print("Thanks for using this guessing number game")


















