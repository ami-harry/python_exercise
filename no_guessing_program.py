# ask the user how many times he wants to guess the no

# set a orinal no and take everytime input from the user and say after comparision. it is greater,lesser,or equal
# and say him that n of gueess you take and n no of guesses is left

# or if he give the right answer, give him that he took n no of times to guess the no


original_no = 99

print("\t\t\t welcome to no guessing game")
print()
guess_limit = int(input("How many times you want to try: "))

print("You have only ", guess_limit, " time to guess the correct no ")
print()

no_of_guess = 1
while no_of_guess <= guess_limit:
    usr_guess = int(input("Enter your guess no: "))

    if usr_guess < original_no:
        print("Your guess no is smaller then the original no: ")
        print("you have tried ", no_of_guess, " times and you have ",
              (guess_limit-no_of_guess), " chances left")
        print()
    elif usr_guess > original_no:
        print("Your guess no is greate  r then the original no: ")
        print("you have tried ", no_of_guess, "times and you have ",
              (guess_limit-no_of_guess), " chances left")
        print()
    else:
        print("Your input is correct  ")
        print(' you won')
        print("You took ", no_of_guess, " times to guess the no")
        print("You have ", (guess_limit - no_of_guess), " times are left")
        print()
        break
    no_of_guess += 1

    if(no_of_guess > guess_limit):
        print("You have exceed the guess limit")
        print("You have ", (guess_limit - no_of_guess), "times are left")
        print('game over')
