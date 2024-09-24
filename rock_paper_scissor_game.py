"""
PROJECT WORKFLOW:

> OUTPUT:
    1. Input form the user(Rock, Paper, Scissor)
    2. Computer choice (Computer will choose rendomly amoung the choices)
    3. Result

    > CASES:
    1.  A - ROCK
        Rock - Rock = Tie
        Rock - Paper = Paper win
        Rock - Scissor = Rock win

    2.  B - PAPER
        Paper - Paper = Tie
        Paper - Rock = Paper win
        Paper - Scissor = Scissor win

    3.  C - SCISSOR
        Scissor - Scissor = Tie
        Scissor - Rock = Rock win
        Scissor - Paper = Scissor win

"""

#Python has a built-in module that you can use to make random numbers
import random

item_list=['Rock','Paper','Scissor']
User_choice=input("Enter your move [Rock, Paper, Scissor] :")
comp_choice=random.choice(item_list)

# The purpose of using a f string is to print the variable in string
print(f"User choice= {User_choice}, Computer choice={comp_choice}")

if (User_choice==comp_choice):
    print("Both chooses are same. \n***Match TIE***")
elif User_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper Covers Rock. \n***COMPUTER WIN***")
    else:
        print("Rock Smashes Scissor. \n***YOU WIN*** ")

elif User_choice=="Paper":
    if comp_choice=="Rock":
        print("Paper Covers Rock. \n***YOY WIN***")
    else:
        print("Rock Smashes Scissor. \n***COMPUTER WIN*** ")

elif User_choice=="Scissor":
    if comp_choice=="Paper":
        print("Scissor Cuts Paper. \n***YOU WIN***")
    else:
        print("Rock Smashes Scissor. \n***COMPUTER WIN*** ")
    



