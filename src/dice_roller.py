"""
dice_roller.py

A simple PyQt6 application that rolls a specified number of D6 (six-sided dice) when a button is clicked,
applies a modifier to the results, and displays the roll results, modifiers, and end results in a label
with a fixed-width font.

To run this script, you need to have PyQt6 installed. You can install it using pip:
    pip install PyQt6
"""

import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QFont
import roll_modifier

class DiceRoller(QWidget):
    """
    A QWidget-based class to create a window with a button that rolls a specified number of D6,
    applies modifiers, and displays the results.
    """
    def __init__(self):
        """
        Initializes the DiceRoller UI by setting up the layout, button, and labels.
        """
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        Sets up the UI components: window title, layout, input boxes, button, and labels.
        """
        self.setWindowTitle('D6 Dice Roller')
        
        self.layout = QVBoxLayout()
        
        self.input_layout = QHBoxLayout()
        self.num_dice_label = QLabel('Number of dice:', self)
        self.input_layout.addWidget(self.num_dice_label)

        self.num_dice_input = QLineEdit(self)
        self.input_layout.addWidget(self.num_dice_input)
        
        self.layout.addLayout(self.input_layout)

        self.modifier_input_layout = QHBoxLayout()
        self.str_modifier_label = QLabel('Modifier:', self)
        self.modifier_input_layout.addWidget(self.str_modifier_label)

        self.str_modifier_input = QLineEdit(self)
        self.modifier_input_layout.addWidget(self.str_modifier_input)

        self.layout.addLayout(self.modifier_input_layout)

        self.roll_button = QPushButton('Roll the Dice', self)
        self.roll_button.clicked.connect(self.roll_dice)
        self.layout.addWidget(self.roll_button)
        
        big_font = QFont('Courier', 20)  # Increased font size to 20

        self.result_label = QLabel('Roll results: ', self)
        self.result_label.setFont(big_font)
        self.layout.addWidget(self.result_label)

        self.modifier_label = QLabel('Modifier: ', self)
        self.modifier_label.setFont(big_font)
        self.layout.addWidget(self.modifier_label)

        self.end_result_label = QLabel('End results: ', self)
        self.end_result_label.setFont(big_font)
        self.layout.addWidget(self.end_result_label)
        
        self.success_count_label = QLabel('Success: ', self)
        self.success_count_label.setFont(big_font)
        self.layout.addWidget(self.success_count_label)
        
        self.failure_count_label = QLabel('Failure: ', self)
        self.failure_count_label.setFont(big_font)
        self.layout.addWidget(self.failure_count_label)

        self.setLayout(self.layout)
        
    def roll_dice(self):
        """
        Generates a random number between 1 and 6 for each die, sorts the results,
        applies the modifier, and updates the result labels.
        """
        try:
            num_dice = int(self.num_dice_input.text())
            if num_dice <= 0:
                raise ValueError("The number of dice must be a positive integer.")
        except ValueError as e:
            self.result_label.setText(f'Error: {e}')
            self.modifier_label.setText('')
            self.end_result_label.setText('')
            return
        
        roll_results = [random.randint(1, 6) for _ in range(num_dice)]
        roll_results.sort()
        roll_results_str = ''.join(f'[{result}]' for result in roll_results)

        str_modifier = int(self.str_modifier_input.text())

        modifier, end_result, success_count, failure_count  = roll_modifier.modify(roll_results, str_modifier)

        self.result_label.setText(f'Roll results:   {roll_results_str}')
        self.modifier_label.setText(f'Modifier:       {modifier}')
        self.end_result_label.setText(f'End results:    {end_result}')
        self.success_count_label.setText(f'Success:    {success_count}')
        self.failure_count_label.setText(f'Failure:    {failure_count}')

def main():
    """
    The main function that initializes the QApplication, creates and shows 
    the DiceRoller window, and starts the application event loop.
    """
    app = QApplication(sys.argv)
    window = DiceRoller()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
