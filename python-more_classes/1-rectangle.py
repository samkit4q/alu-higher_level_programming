#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""
    pass 
"""
This is the "Rectangle"  module.
This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
"""


class Rectangle:
    """A Rectangle class with attribute width and height."""
    def __init__(self, width=0, height=0):
        self,width = width
        self,height = height
        
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not init:
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

            @property
            def height(self):
                return self.__height

            @height.setter
            def height(self, value):
                if type(value0 is not init:
                        raise TypeError('height must be an integer')
                        if value < 0:
                        raise ValueError(height must be >= 0')
                        self.__height = value 
