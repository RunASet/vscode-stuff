# Function Definitions
import random

##
#   function: first_choice(int)
#
#   input: int data type that represents the first selection the user made
#
#   return: int data type represents preceding choice
##

def first_choice(n):   # Acts as a switch case statement that will check all the possible choices and return The next dialouge box for the user
    if n == 1:         # Choice for Events
        print("\n-------------------------------------\n",
              "Event Tables\n", "\b-------------------------------------\n")
        return int(input("(1) Travel\n\n(2) Dungeon\n\n(3) Town/Village\n\n(4) City\n\nInput (1-4)"))
    else:
        return 0
##
#   function: travel_events()
#
#   input: no input
#
#   return: no return
#
#   Purpose: 

def travel_events():
    print("\n-------------------------------------\n",
          " Travel Event Tables\n", "\b-------------------------------------\n")
    n = int(input("Where are you travelling?\n\n(1) Desert\n\n(2) Ocean\n\n(3) Mountain\n\n(4) Random\n\nSelect (1-4)"))

    if n == 1:
        
        print(random.randint(1,500)) # Is the random number that is set of a range that is as large as all the tables put together
        # desert_Array[] = rand() need to figure out what this will be gonna use a Dict to figure it out
    elif n == 2:
        
        print(random.randint(1,500)) # Is the random number that is set of a range that is as large as all the tables put together
        # Ocean_Array[] = rand() need to figure out what this will be gonna use a Dict to figure it out    
    elif n == 3:
        
        print(random.randint(1,500)) # Is the random number that is set of a range that is as large as all the tables put together
        # mountain_Array[] = rand() need to figure out what this will be gonna use a Dict to figure it out
    elif n == 4:
        
        print(random.randint(1,500)) # Is the random number that is set of a range that is as large as all the tables put together
        # all_arrays_combined_Array[] = rand() need to figure out what this will be gonna use a Dict to figure it out
##
#   function: error_check
#
#   input: int data type
#
#   return: true or false
#
#   purpose: check if the user input a incorrect value
##
def error_check(n):
    if n > 0:
        return n
    else:
        print("Try Again buddy!!\n")
        n = int(input("Reinput what you want DO IT RIGHT: "))
        if n <= 0:
            print("No more of this!!")
            return -1
        else:
            return n
##
#   function: checker(int)
#
#   Input: int data type, representing the very first number input from the user
#
#   return: Returns number that will be used to summon the array that holds the respective table
##
def checker(n):
    if n == 1:
        x = first_choice(n)
        if x <= 0 or x > 4:
            return 0
        if x == 1:
            # The travel event function will then expand to allow the user to select different climates or roll on a mass table
            return travel_events()