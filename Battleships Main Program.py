# Battleships_Main_Program.py
# @ Timothy Tomas -420190086- 2019
# @ Chris Moody -420190047- 2019
# Date: 07/06/19
# Description: Main program for Battle Ships game

# importing classes
import time 
from Command import Command
from Ship import Ship
from Map import Map

# welcome screen
print("""
      ██████╗  █████╗ ████████╗████████╗██╗     ███████╗
      ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
      ██████╔╝███████║   ██║      ██║   ██║     █████╗
      ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
      ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
      ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
            ███████╗██╗  ██╗██╗██████╗ ███████╗      
            ██╔════╝██║  ██║██║██╔══██╗██╔════╝      
            ███████╗███████║██║██████╔╝███████╗
            ╚════██║██╔══██║██║██╔═══╝ ╚════██║
            ███████║██║  ██║██║██║     ███████║      
            ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝
                     By: TT and CM
      """)

print("\n\n")
print("Welcome to Battle Ships!")

print("""
In this game, you will be able to complete
the first phase of a Battle Ships game.
You will be asked to place two ships on a 5x5 grid. Each ship is 3 coordinates long.
You can choose to place ships, show the map of the sea, or the coordinates of your ships.\n""")

# shows the user what valid coordinates exist on the map
print("Here is a table of coordinates to make your experience better!\nYou can view this table again by typing 'T' suring the command prompt.\n")

# creats a visual representation of the coordinates map
game_map = Map()
game_map.show_coordinates()

# creating commands
placing_ship_1 = Command()
placing_ship_2 = Command()

# creating ship object
ship = Ship()

# setting number of ships on map to zero
ship_count = 0

# creating a loop - game will run until the exit command is called
is_running = True
while is_running:
    print("""
Key:
C: Show ship coordinates
P: Place ships
S: Show sea
T: Show table of coordinates
Q: Quit program
    """)
    # getting user input for commands and calling appropraite function
    command_type = input ("Enter a command:\n").title()
    
    if command_type == "Q":    # calls the exit_game funciton from the command class
        Command.exit_game()
        
    elif command_type =="P":    # calls the exit_game funciton from the command class
        if ship_count == 0:
            print("\n")
            print("Placing your first ship:\n")
            placing_ship_1.place()    # calls the place funciton from the command class for placing_ship_1 object
            ship_count += 1
            
        elif ship_count == 1:    # allows this place funciton for the placing_ship_2 object after placing_ship_1 object has been made
            print("\n")
            print("Placing your second ship:\n")
            placing_ship_2.place()     # calls the place funciton from the command class for placing_ship_2 object
            ship_count += 1
            
        else:
            print("\nMaximum number of ships on board!")

    elif command_type =="C":    # prints the coordinates of the ships that have been placed
        print("\n")
        print("Location of ship 1:",Ship._ship_location[0:3])
        print("Location of ship 2:",Ship._ship_location[3:6])

    elif command_type =="S":    # calls the show_grid funciton (visual representaiton) to display all ships placed on the map
        print("\n")
        ship.show_grid()
        print("\n")

    elif command_type =="T":    # calls the show_grid funciton (visual representaiton) to display all ships placed on the map
        print("\n")
        game_map.show_coordinates()
        print("\n")
        
    else:
        print("\nThat is not a recognised command.\n")

    


