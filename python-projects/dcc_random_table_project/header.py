# constant variables
CONST_MIN_RANGE_SIZE = 0


# Function Definitions
import random
##
#   Function: roll_Again()
#
#   input: none
#
#   variables: string data type, y == variable that will hold what the user wants to unput   
#   
#   return: 0
#
#   purpose: makes it so user can choose to roll multiple times on the respective table they are currently rolling on.
##
def roll_Again():
    y = str(input("Do you wish to roll again (y/n)? "))
    if y != 'y' and y !='Y':
        return 0
##
#   Function: range_of_table(int,int,int)
#
#   input: n = user_input,x = min_range,y = max_range
#
#   variables:    
#   
#   return: 0 or n
#
#   purpose: makes sure that the table size is not being over done
##
def range_of_table(n,x,y):
    if n <= x or n > y:
            return 0
    else:
        return n
    
### Events class holds everything that is used in relation to the Events selection    
class Events:        
    _SIZE_OF_EVENT_TABLE = 4          # Attribute size of the Event table
    _SIZE_OF_TRAVEL_EVENT_TABLE = 4
    ##
    #   Method: events_(int)
    #
    #   input: int data type that represents the first selection the user made
    #
    #   return: int data type represents preceding choice
    #
    #   purpose: recieves value from the 
    ##
    def events_():   
                 # Choice for Events
        print("\n-------------------------------------\n",
                "Event Tables\n", "\b-------------------------------------\n")
        return int(input("(1) Travel\n\n(2) Dungeon\n\n(3) Town/Village\n\n(4) City\n\nInput (1-4)"))
    ##
    #   method: travel_events()
    #
    #   input: no input
    #
    #   return: no return
    #
    #   Purpose: Provides the optiosn for all of the travel events

    def travel_events():
        print("\n-------------------------------------\n",
            " Travel Event Tables\n", "\b-------------------------------------\n")
        n = int(input("Where are you travelling?\n\n(1) Desert\n\n(2) Ocean\n\n(3) Mountain\n\n(4) Random\n\nSelect (1-4)"))

        n = range_of_table(n,CONST_MIN_RANGE_SIZE,Events._SIZE_OF_TRAVEL_EVENT_TABLE)     
        if n == 1:
            i = 1
            while i == 1:
                print(random.randint(1,500))  # random number range of the respective table, user may change these to incorporate new choices
                # the random integer will equal the dictionary here
                if roll_Again() == 0:
                    i -= 1
                    return 0
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
#   return: Returns either 0 or 1 to signal if running should stop
#
#   purpose: will direct the user to respective big tables, this is mega table
##
def checker(n):
    n = range_of_table(n,CONST_MIN_RANGE_SIZE,4)
    if n == 1:
        x = range_of_table(Events.events_(),CONST_MIN_RANGE_SIZE,Events._SIZE_OF_EVENT_TABLE)
        if x == 1:
            # The travel event method will then expand to allow the user to select different climates or roll on a mass table
            return Events.travel_events()


