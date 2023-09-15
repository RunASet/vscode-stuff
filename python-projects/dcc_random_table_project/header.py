# constant variables
CONST_MIN_RANGE_SIZE = 0


# Function Definitions
import events
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
        x = range_of_table(events.events_(),CONST_MIN_RANGE_SIZE,events._SIZE_OF_EVENT_TABLE)
        if x == 1:
            # The travel event method will then expand to allow the user to select different climates or roll on a mass table
            return events.travel_events()


