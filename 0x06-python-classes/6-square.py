#!/usr/bin/python3
"""class of square"""
class Square:
    """define the class"""
    def __init__(self, size=0, position=(0, 0)):
        """attributes
        size: size of square
        """
        self.size = size
        self.position = position
        
    def area(self):
        """
        Return the area of square
        """
        return self.__size**2
    @property
    def size(self):
        """
        return size as getter method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size using setter method
        """
        self.__size = value
        if type(value) != int:
             raise TypeError("size must be an integer")
        if value < 0:
             raise ValueError("size must be >= 0")
    @property
    def position(self):
        """
        getter method
        """
        return self.__position
    @position.setter
    def position(self, value):
        """
        setter method
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        print square positions
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
        elif self.__size == 0:
            print()

