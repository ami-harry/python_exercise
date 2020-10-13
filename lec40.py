# exercise 6
# game
# snake, water, gun

# if a is water and b is gun--> water will win, becuase the gun will sink into the water
# if a is gun and b is snake--> a will win, gun will shot the snake
# if a is snake and b is water--> snake will win, snake will drink the water

# make a game using while loop and play the game 10 time and declare who wins how much times and print th final results
# use random.choice() module


import random
print("\t\t\t\t\tSnake water gun game")

opt = ['s', 'w', 'g']

chances = 10
no_of_chances = 0
computer_point = 0
human_point = 0

while no_of_chances < chances:
    usr_inp = input("Enter s for snake\tw for water\tg for gun\n")
    comp_inp = random.choice(opt)

    if usr_inp == comp_inp:
        print("Tie, Both got 0 point")

    # if user inputs s
    elif usr_inp == 's' and comp_inp == 'w':
        human_point = human_point + 1
        print(f"User input was {usr_inp} and computer option was {comp_inp}")
        print("the snake will drink water")
        print("human won, human got 1 point")

    elif usr_inp == 's' and comp_inp == 'g':
        computer_point = computer_point + 1
        print(f"User input was {usr_inp} and computer option was {comp_inp}")
        print("computer won, computer got 1 point")
        print("gun will shot the snake")

    # if user inputs g
    elif usr_inp == 'g' and comp_inp == 's':
        human_point = human_point + 1
        print(f"User input was {usr_inp} and computer option was {comp_inp}")
        print("humans won, human got 1 point")
        print("gun will shot the snake")

    elif usr_inp == 'g' and comp_inp == 'w':
        computer_point = computer_point + 1
        print(f"User input was {usr_inp} and computer option was {comp_inp}")
        print("computer won , computer  got 1 point")
        print("gun will shink into water")

    # if user inputs w
    elif usr_inp == 'w' and comp_inp == 's':
        computer_point = computer_point + 1
        print(f"User input was {usr_inp} and computer option was {comp_inp}")
        print("computer won, computer got 1 point")
        print("snake will drink the snake")

    elif usr_inp == 'w' and comp_inp == 'g':
        human_point = human_point + 1
        print(f"User input was {usr_inp} and computer option was {comp_inp}")
        print("human, human got 1 point")
        print("gun will sink into water")
    else:
        print("Enter valid option")

    no_of_chances = no_of_chances+1
    print(f"{chances - no_of_chances} chance is left out of {chances} chances \n")

if computer_point == human_point:
    print("game tie")
    print(
        f"both got same points\n computer has {computer_point} points and human has {human_point}")

elif computer_point > human_point:
    print("Computer won ")
else:
    print("you won")
print(f"you got {human_point} points and computer got {computer_point} points")
