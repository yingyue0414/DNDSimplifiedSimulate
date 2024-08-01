"""
Start the dice_roller.py

A simple PyQt6 application that rolls a specified number of D6 (six-sided dice) when a button is clicked,
applies a modifier to the results, and displays the roll results, modifiers, and end results in a label
with a fixed-width font.

To run this script, you need to have PyQt6 installed. You can install it using pip:
    pip install PyQt6
"""

import sys
import src.dice_roller as dr

if __name__ == '__main__':
    dr.main()