# binary search
# take input from the user and say him and say if no is greater
# if less then say that input is less
# is match , your correct
# no of guesses must be fixed
# print no of guesses


original_number = 45

print("\t\t\tWelcome to no guessing program")
print("No of guesses is limited to 9! ")
no_of_guess_time = 1
while(no_of_guess_time <= 9):
    usr_inp = int(input("Enter your guess no:  "))
    if usr_inp > original_number:
        print("Your input is greater than the original no: ")
        print("You have tried ", no_of_guess_time,
              " times you have ", (9-no_of_guess_time), " is left only")
        print()
    elif usr_inp < original_number:
        print("Your input is smaller than the original no: ")
        print("You have tried ", no_of_guess_time,
              " times you have ", (9-no_of_guess_time), " is left only")
        print()
    else:
        print("Your guess is correct: ")
        print("You Won")
        print("You have tried ", no_of_guess_time,
              " times you have ", (9-no_of_guess_time), " is left only")

        print()
        break
        print("No of guesses is left ", no_of_guess_time-1)
    no_of_guess_time += 1

    if no_of_guess_time > 9:
        print("You have exceed the guess limit")
        print("Game over!")
