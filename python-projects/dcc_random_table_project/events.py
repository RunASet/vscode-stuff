import header
import random
import desert
import ocean
import mountain
import travel_random

### Events class holds everything that is used in relation to the Events selection    
class Events():        
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
    #   Purpose: Provides the options for all of the travel events
    ##
    def travel_events():
        print("\n-------------------------------------\n",
            " Travel Event Tables\n", "\b-------------------------------------\n")
        n = int(input("Where are you travelling?\n\n(1) Desert\n\n(2) Ocean\n\n(3) Mountain\n\n(4) Random\n\nSelect (1-4)"))

        n = header.range_of_table(n,header.CONST_MIN_RANGE_SIZE,Events._SIZE_OF_TRAVEL_EVENT_TABLE)     
        if n == 1:
            i = 1
            while i == 1:
                print("\n\n--------------------\nencounter\n--------------------\n",
                      desert.DESERT_TRAVEL_EVENTS.get(random.randint(1,desert.SIZE_OF_DESERT)),
                      "\n\n") 
                # random number range of the respective table, user may change these to incorporate new choices
                # the random integer will equal the desert dictionary index here, to be added later, print is for debugging
                # use get() method for getting the dictionary values
                if header.roll_Again() == 0:
                    i -= 1
                    return 0
        elif n == 2:
            i = 1
            while i == 1:
                print("\n\n--------------------\nencounter\n--------------------\n",
                      mountain.MOUNTAIN_TRAVEL_EVENTS.get(random.randint(1,4)),
                      "\n\n")  
                # random number range of the respective table, user may change these to incorporate new choices
                # the random integer will equal the Ocean dictionary here
                if header.roll_Again() == 0:
                    i -= 1
                    return 0
        elif n == 3:
            i = 1
            while i == 1:
                print("\n\n--------------------\nencounter\n--------------------\n",
                      ocean.OCEAN_TRAVEL_EVENTS.get(random.randint(1,4)),
                      "\n\n")  
                # random number range of the respective table, user may change these to incorporate new choices
                # the random integer will equal the Moutain dictionary here
                if header.roll_Again() == 0:
                    i -= 1
                    return 0
        elif n == 4:
            i = 1
            while i == 1:
                print("\n\n--------------------\nencounter\n--------------------\n",
                      travel_random.RANDOM_TRAVEL_EVENTS.get(random.randint(1,4)),
                      "\n\n")  
                # random number range of the respective table, user may change these to incorporate new choices
                # the random integer will equal the Random dictionary here
                if header.roll_Again() == 0:
                    i -= 1
                    return 0
        else:
            return 0
