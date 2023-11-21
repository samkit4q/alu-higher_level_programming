 #!/usr/bin/python3
"""Define a class square."""


class square:
    """Represent a square."""
    
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size(int): The sixe of a new square.
        """
         if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueEroror("size must be >= 0")
        self.__size = size
