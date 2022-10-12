# random library for generating the random number
import random

# function if user chooses Hard Game
# here range of number will be from 1 to 500
def hardGame():
    # guess the random number using random.randint to be guessed by user
    guess = random.randint(1,500)
    # chanceNumber is the random number which will not decrement 
    # the number of tries available for the user.
    chanceNumber = random.randint(1,500)
    # number of tries available for user 
    # you can change this number according to your need
    tries = 5
    print("\nYou have 5 tries\nGuess number between 1 to 500")
    # loop till the number of tries not decrements to 0
    while(tries!=0):
        # user input for guessing the number
        userInput = int(input())
        # if user guesses the correct number then the user won
        if(userInput == guess):
            print("You won")
            break
        # if user guess the number greater than the random number
        # it will show input is high
        elif(userInput > guess):
            # if input user is equals to the chance Number then 
            # the tries variable will not get decremented
            if (userInput == chanceNumber):
                print("No chance decremented\n")
                print("You have ", tries, " tries left")
            # if not equals to chance number 
            # then tries variable get decremented
            else:
                print("Input is High\n")
                tries = tries - 1
                print("You have ", tries, " tries left")
        # if user guess the number less than the random number
        # it will show input is low
        elif(userInput < guess):
            # same thing will happen if user input is equals to chance number
            if (userInput == chanceNumber):
                print("No chance decremented")
                print("You have ", tries, " tries left")
            else:
                print("Input is Low\n")
                tries = tries - 1
                print("You have ", tries, " tries left")          

# function if user chooses Moderate Game
# here range of number will be from 1 to 200
# the logic will remain same as hardGame function
# only range changes
def moderateGame():
    guess = random.randint(1,200)
    chanceNumber = random.randint(1,200)
    tries = 5
    print("You have 5 tries\nGuess number between 1 to 200")
    while(tries!=0):
        userInput = int(input())
        if(userInput == guess):
            print("You won")
            break
        elif(userInput > guess):
            if (userInput == chanceNumber):
                print("No chance decremented\n")
                print("You have ", tries, " tries left")
            else:
                print("Input is High\n")
                tries = tries - 1
                print("You have ", tries, " tries left")
        elif(userInput < guess):
            if (userInput == chanceNumber):
                print("No chance decremented")
                print("You have ", tries, " tries left")
            else:
                print("Input is Low\n")
                tries = tries - 1
                print("You have ", tries, " tries left")

# function if user chooses Easy Game
# here range of number will be from 1 to 50
# the logic will remain same as hardGame function
# only range changes
def easyGame():
    guess = random.randint(1,50)
    chanceNumber = random.randint(1,50)
    print(guess, "  ", chanceNumber)
    tries = 5
    print("You have 5 tries\nGuess number between 1 to 50")
    while(tries!=0):
        userInput = int(input())
        if(userInput == guess):
            print("You won")
            break
        elif(userInput > guess):
            if (userInput == chanceNumber):
                print("No chance decremented\n")
                print("You have ", tries, " tries left")
            else:
                print("Input is High\n")
                tries = tries - 1
                print("You have ", tries, " tries left")
        elif(userInput < guess):
            if (userInput == chanceNumber):
                print("No chance decremented")
                print("You have ", tries, " tries left")
            else:
                print("Input is Low\n")
                tries = tries - 1
                print("You have ", tries, " tries left")

# difficulty level will be shown to the user 
# and then asked to select the difficulty level 
# .lower() is done so that if user enters H
# then it coverts capital H to small h
difficulty = input('''1. For hard enter H or h
2. For moderate enter M or m
3. For easy enter E or e
Enter the difficulty level: ''').lower()

print("If you guess the Chance Number then number of try will not be decremented")

# here the hardGame, moderateGame, easyGame function is called 
# based upon the user input
if (difficulty == 'h'):
    hardGame()
elif (difficulty == 'm'):
    moderateGame()
elif (difficulty == 'e'):
    easyGame()
else:
    print("Wrong Input")