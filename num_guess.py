from numpy import random

x = random.randint(10000)

def num_guesser(x, loops):
    "Makes the user guess what number the program is thinking of"
    y = 0
    if loops == 0:
        print("I am thinking of a number from 0 to 10,000. Can you guess what it is?")
    y = int(input("Guess:"))
    if y == x:
        print("You got it!")
        return True
    elif int(y) < 0 or int(y) > 10000:
        print("Please pick a number between 0 and 10,000")
        loops += 1
        num_guesser(x,loops)
    elif int(y) < x:
        print("Too low!")
        loops += 1
        num_guesser(x,loops)
    else: #int(y) > x:
        print("Too high!")
        loops += 1
        num_guesser(x,loops)
    # else:
    #     print("Please enter an integer between 0 and 10,000")
    #     num_guesser(x,loops)
        
num_guesser(x,0)

# Human enters number, computer tells if higher or lower, then runs again until the human guesses correctly
# Additional idea: Save guessed numbers and make it comment if guessed again