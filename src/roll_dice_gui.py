"""
A simple GUI application to roll a six-sided die (D6) using tkinter.

This module provides a graphical interface where users can click a button to roll
a D6 die and see the result displayed in the window.

Functions:
    roll_dice: Rolls a D6 and updates the result label with the outcome.
"""

import tkinter as tk
import random

def roll_dice():
    """
    Roll a D6 and display the result in the result label.

    This function generates a random number between 1 and 6, simulating the roll
    of a six-sided die. The result is then displayed in the result_label widget.
    """
    result = random.randint(1, 6)
    result.config(text=f'Result: {result}')

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("D6 Dice Roller")

    # Create and place the roll button
    roll_button = tk.Button(root, text="Roll D6", command=roll_dice)
    roll_button.pack(pady=10)

    # Create and place the result label
    result_label = tk.Label(root, text="Result: ", font=('Helvetica', 18))
    result_label.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()
