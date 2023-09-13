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
## Function Definitions, need to make a header file later

"""
Function: first_choice

Input: int data type that represents the first selection the user made



""" 
def first_choice(n):   # Acts as a switch case statement that will check all the possible choices and return The next dialouge box for the user
    if n == 1:         # Choice for Events
        print("\n-------------------------------------\n","Event Tables\n","\b-------------------------------------\n")
        return int(input("(1) Travel\n\n(2) Dungeon\n\n(3) Town/Village\n\n(4) City"))
    else:
        return 1
## Main function    
print("\n-------------------------------------\n","DCC Random Tables\n","\b-------------------------------------\n")

choice = int(input("Select what type of table do you want:\n\n(1) Events\n\n(2) Encounters\n\n(3) Magic/Gods\n\n(4) Equipment\n\n(5) Random\n\nSelect(1-5): "))
print('\n\n')




# The following will be the future choices that will be given to the user (1) Over-World Travel Events\n\n(2) Dungeon Encounters\n\n(3)"