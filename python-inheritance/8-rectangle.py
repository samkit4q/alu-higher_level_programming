#!/usr/bin/python3
class BaseGeometry:
    def integer_validator(self, name, value):
        """Validate that the value is a positive integer."""
        if type(value) is not int or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

# 9-rectangle.py
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Validate width and height as positive integers
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Set private attributes
        self.__width = width
        self.__height = height
