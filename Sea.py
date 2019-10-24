# Sea.py
# @ Timothy Tomas -420190086- 2019
# @ Chris Moody -420190047- 2019
# Date: 07/06/19
# Description: Sea class for Battle Ships game - sets sea size

class Sea():

    # initialising Sea class attributes
    def __init__(self):
        self.__x_sea_size = 5
        self.__y_sea_size = 5
        self.__show_sea_size = str

    @property    # getter for x_sea_size
    def x_sea_size(self):
        return self.__x_sea_size

    @property    # getter for y_sea_size
    def y_sea_size(self):
        return self.__y_sea_size

    @x_sea_size.setter    # setter for x_sea_size
    def x_sea_size(self, value):
        self.__x_sea_size = value

    @y_sea_size.setter    # setter for y_sea_size
    def y_sea_size(self, value):
        self.__y_sea_size = value





