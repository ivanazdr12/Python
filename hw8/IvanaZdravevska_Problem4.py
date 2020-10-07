# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 08, October 21, 2019

#Problem 4
import random
randomNumber = random.randrange(0,50)
print("I’m thinking of a number in the range 0-50. You have five tries to guess it.")
guessed = False
count = 0
guesses = 1
while guessed is False and count < 5:
    userInput = int(input("Guess " + str(guesses) + "? "))
    guesses +=1
    count += 1
    if userInput == randomNumber:
        guessed = True
        print('You are correct! I was thinking of ' + str(randomNumber))
        break
    elif userInput > randomNumber:
        print(str(userInput) + " is too high.")
    elif userInput < randomNumber:
        print(str(userInput) + " is too low.")
    if count == 5:
        print("Your guess is incorrect. The right answer is " + str(randomNumber))
        print("End of program")
