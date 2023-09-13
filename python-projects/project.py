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
print("\n-------------------------------------\n","DCC Random Tables\n","\b-------------------------------------\n")

choice = int(input("Select what type of table do you want:\n\n(1) Events\n\n(2) Encounters\n\n(3) Magic\n\n(4) Equipment\n\n(5) Random\n\nSelect(1-5): "))
print('\n\n')
if choice == 1:
    newchoice = int(input("What would you:"))

# The following will be the future choices that will be given to the user (1) Over-World Travel Events\n\n(2) Dungeon Encounters\n\n(3)"