# Map.py
# @ Timothy Tomas -420190086- 2019
# @ Chris Moody -420190047- 2019
# Date: 04/06/19
# Description: Map class for Battle Ships game

class Map():

    # all available coordinates on board 
    _map_positions = [(0,4), (1,4), (2,4), (3,4), (4,4),
                      (0,3), (1,3), (2,3), (3,3), (4,3),
                      (0,2), (1,2), (2,2), (3,2), (4,2),
                      (0,1), (1,1), (2,1), (3,1), (4,1),
                      (0,0), (1,0), (2,0), (3,0), (4,0)]

    # fuction that prints out the map
    def show_coordinates(self):
        print(self._map_positions [0:5])
        print(self._map_positions [5:10])     
        print(self._map_positions [10:15])   
        print(self._map_positions [15:20])
        print(self._map_positions [20:25])
