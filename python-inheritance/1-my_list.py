#!/usr/bin/python3
"""Module defining the MyList class."""

class MyList(list):
    """Inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))

# Example usage:
if __name__ == "__main__":
    my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    
    # Print the original list
    print("Original List:", my_list)

    # Use the print_sorted method
    my_list.print_sorted()

