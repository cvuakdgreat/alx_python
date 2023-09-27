"""
Creating a class named Square
"""
class Square:
    """
    this is a class that defines a square

    Attributes:
        size: int value
    """    
    def __init__(self, size=0):
        """
        this is the init method of the class square
            Arg:
                size
            Returns:
                raises error if not an interger
                raises error if valve not greater than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be > 0")
        self.__size = size