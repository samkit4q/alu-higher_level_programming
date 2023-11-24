#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry."""
class BaseGeometry:
    """BaseGeometry class."""
    def integer_validator(self, name, value):
        """Validate that the value is a positive integer."""
        if type(value) is not int or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

# Printing the directory of the Rectangle class
print(dir(Rectangle))

