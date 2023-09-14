"""
Programmer: Zeno Enderle

Date: 9/13/2023

filename: project.py // potential header file

purpose: create a program that stores every single random roll table from all the DCC material I have.
The program will roll for the table and will also be able to take a input representitive of the dice roll.
The point is to provide a faster and more random experience overall while sticking true to the source material.

Future Goals: Make it so I have a website similar to 5etools, Will have blocks user can click on to take them to the table choices
So that the User will not have to manually input the command into the terminal.
"""
# Function Definitions, need to make a header file later

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


def travel_events():
    print("\n-------------------------------------\n",
          " Travel Event Tables\n", "\b-------------------------------------\n")
    n = int(input("Where are you travelling?\n\n(1) Desert\n\n(2) Ocean\n\n(3) Mountain\n\n(4) Random\n\nSelect (1-4)"))

    if n == 1:
        print("You're a test")
        # desert_Array[] = rand() need to figure out what this will be gonna use a Dict to figure it out


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


# Main function
print("\n-------------------------------------\n",
      "DCC Random Tables\n", "\b-------------------------------------\n")
i = 1
while i == 1:
    choice_1 = int(input(
        "Select what type of table do you want:\n\n(1) Events\n\n(2) Encounters\n\n(3) Magic/Gods\n\n(4) Equipment\n\n(5) Random\n\nSelect(1-5): "))
    print('\n\n')

    # Checks to see if there is an invalid input will stop loop
    if error_check(choice_1) <= 0 or error_check(choice_1) > 5:
        i -= 1
    choice_1 = error_check(choice_1)

    choice_2 = checker(choice_1)


# The following will be the future choices that will be given to the user (1) Over-World Travel Events\n\n(2) Dungeon Encounters\n\n(3)"
