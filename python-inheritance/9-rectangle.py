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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

# Example usage:
if __name__ == "__main__":
    my_rectangle = Rectangle(5, 10)

    # Testing area method
    print(f"Area of the rectangle: {my_rectangle.area()}")

    # Testing __str__ method
    print(my_rectangle)
