# Ship.py
# @ Timothy Tomas -420190086- 2019
# @ Chris Moody -420190047- 2019
# Date: 07/06/19
# Description: Ship class for Battle Ships game - sets ship attributes

from Sea import Sea

class Ship():
    
    # creates a list of possible coordinates
    _ship_position = [(0,4), (1,4), (2,4), (3,4), (4,4),
                      (0,3), (1,3), (2,3), (3,3), (4,3),
                      (0,2), (1,2), (2,2), (3,2), (4,2),
                      (0,1), (1,1), (2,1), (3,1), (4,1),
                      (0,0), (1,0), (2,0), (3,0), (4,0)]


    # creates a list that is used as the GUI
    _display_position = [" ~ "," ~ "," ~ "," ~ "," ~ ",
                         " ~ "," ~ "," ~ "," ~ "," ~ ",
                         " ~ "," ~ "," ~ "," ~ "," ~ ",
                         " ~ "," ~ "," ~ "," ~ "," ~ ",
                         " ~ "," ~ "," ~ "," ~ "," ~ "]
    
    # creates a list which will store ship coordinates created in the place function
    _ship_location = []

    # fuction that prints out the GUI
    def show_grid(self):
        row_5 = "".join(self._display_position [0:5])
        print(row_5)
        row_4 = "".join(self._display_position [5:10])
        print(row_4)
        row_3 = "".join(self._display_position [10:15])
        print(row_3)
        row_2 = "".join(self._display_position [15:20])
        print(row_2)
        row_1 = "".join(self._display_position [20:25])
        print(row_1)
        
    # gets an input from the user to determine origin coordinates and direction of ship placement
    def place(self):
        invalid_input = True    # loops the input block until user puts a valid input
        while invalid_input:
            try:
                print("Enter 'H' for horizontal or 'V' for vertical placement,\nthen separate integers for the first x and y coordinate of the ship.")
                print("Seperate values with commas (e.g. 'H,0,0').\n")
                str, x, y = input("Please enter ship placement key:\n").split(",")    # getting input...
                str = str.title()
                x_input = int(x)
                y_input = int(y)
                
                # calculates ships 3 coordinates based on the user specified direction and origin coordinates 
                if str == "H":
                    ship_coordinates = ((x_input, y_input), (x_input +1, y_input), (x_input +2, y_input))
                elif str == "V":
                    ship_coordinates = ((x_input, y_input), (x_input, y_input +1), (x_input, y_input +2))
                elif str != "V" or str != "H":
                    x_input = 42    # sets x_input to an invalid value to catch if user incorrectly enters a str that is not "H" or "V"

                # makes sure the whole ship is being placed on the board 
                if  x_input == 42:
                    print("\nPlease enter values in the correct format!")
                    print("Ship not placed.\n\n")
                elif str == "H" and x_input +2 > (Sea().x_sea_size-1):
                    print("\nYour ship needs to be on the board!\n")
                elif str == "V" and y_input +2 > (Sea().y_sea_size-1):
                    print("\nYour ship needs to be on the board!\n") 
                # makes sure that the user cannot overlap an existing ship
                elif ship_coordinates[0] not in Ship()._ship_position or ship_coordinates[1] not in Ship()._ship_position or ship_coordinates[2] not in Ship()._ship_position:
                    print("\nCan't place here! Another ship lies on these coordinates.\n")

                # the if statements below do 3 things:
                    # adds ship coordinates to the _ship_location list
                    # alters the _display_position_list (GUI) to show placed ships
                    # alters the _ship_position_list; removes the coordinate value, but keeps its indexed position
                else:
                    invalid_input = False    # loop stops here
                    print("Ship has been placed!")
                    if ship_coordinates[0] in Ship()._ship_position:
                        Ship()._ship_location.append(ship_coordinates[0])
                        ship_origin_index = Ship()._ship_position.index(ship_coordinates[0])
                        Ship()._display_position[ship_origin_index] = " O "
                        Ship()._ship_position[ship_origin_index] = ""

                    if ship_coordinates[1] in Ship()._ship_position:
                        Ship()._ship_location.append(ship_coordinates[1])
                        ship_origin_index = Ship()._ship_position.index(ship_coordinates[1])
                        Ship()._display_position[ship_origin_index] = " O "
                        Ship()._ship_position[ship_origin_index] = ""

                    if ship_coordinates[2] in Ship()._ship_position:
                        Ship()._ship_location.append(ship_coordinates[2])
                        ship_origin_index = Ship()._ship_position.index(ship_coordinates[2])
                        Ship()._display_position[ship_origin_index] = " O "
                        Ship()._ship_position[ship_origin_index] = ""

            except ValueError:    # catch error if user types in a bad input
                print("\nPlease enter values in the correct format!")
                print("Ship not placed.\n\n")
'''
is_running = True
while is_running:
    ss = Ship()
    ss.place()           
'''              
            





        


