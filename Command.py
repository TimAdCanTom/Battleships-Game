# Command.py
# @ Timothy Tomas -420190086- 2019
# @ Chris Moody -420190047- 2019
# Date: 07/06/19
# Description: Command class for Battle Ship program - defines some commands of the game

# importing classes
from Sea import Sea
from Ship import Ship

class Command():

    # checker before quiting completely
    def exit_game():
        end_game = False
        while end_game == False:
            command = input ("Are you sure you want to quit?(Y/N)\n").title()
            if command == "Y":
                exit()
            elif command =="N":
                break
                
    # calls place from class Ship
    def place(self):
        Ship.place(self)


