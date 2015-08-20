import random

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        print "Sorry you passed a wrong choice for player choice."
	quit()

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else:
        print "Sorry, computer generated wrong input."

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    # print out the message for the player's choice
    # convert the player's choice to player_number using the function name_to_number()
    # compute random guess for comp_number using random.randrange()
    # convert comp_number to comp_choice using the function number_to_name()
    # print out the message for computer's choice
    # compute difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message
    print 
    print "Player chooses " + str(player_choice)
    player_choice_number = name_to_number(player_choice)
    number = random.randint(0,4)
    comp_choice = number_to_name(number)
    print "Computer chooses " + str(comp_choice)
    diff = (player_choice_number - number) % 5
    if (diff == 0):
        print "It is a Tie !!!"
    if (diff == 1):
        print "Player wins!"
    if (diff == 2):
        print "Player wins!"
    if (diff == 3):
        print "Computer wins!"
    if (diff == 4):
        print "Computer wins!"
    

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")

#To execute the game until player wants implement a while loop.
option = "Y"
while (option == "Y" or option == "y"):
  input = raw_input("Enter choice from: rock, Spock, paper, lizard, scissor:  ")
  rpsls(input)
  option = raw_input("Do you want to continue? (y/n)")
