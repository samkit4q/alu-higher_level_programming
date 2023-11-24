#!/usr/bin/python3
"""Module defining the Rectangle class."""

class BaseGeometry:
    """BaseGeometry class."""

    def integer_validator(self, name, value):
        """Validate that the value is a positive integer."""
        if type(value) is not int or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.__width = 0  # Initialize to 0, will be set by integer_validator
        self.__height = 0  # Initialize to 0, will be set by integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

# Documentation for the module
"""
Module defining the Rectangle class.
"""

# Documentation for the BaseGeometry class
"""
BaseGeometry class.
"""

# Documentation for the Rectangle class
"""
Rectangle class, inherits from BaseGeometry.
"""

# Documentation for the integer_validator method
"""
Validate that the value is a positive integer.

Args:
    name (str): The name of the value being validated.
    value (int): The value to be validated.

Raises:
    ValueError: If the value is not a positive integer.
"""

# Note: Do not include 'import' or 'from' inside comments as per the instructions.
