import numpy as np

def modify(dice_rolls, str_modifier, success_threshold=4):
    """
    Calculate the number of success and failure dice based on the dice rolls and strength modifier.

    Args:
        dice_rolls (list): List of dice results. Dice must be increasing order!
        str_modifier (int): Strength modifier to adjust the dice results.

    Returns:
        tuple: A tuple containing the number of success dice, failure dice, and adjusted dice results.
    """
    adjusted_rolls = []

    # DICE ROLLS MUST BE IN INCREASING ORDER!
    # Apply positive or negative modifier starting from the highest failure die
    if str_modifier > 0:
        for roll in reversed(dice_rolls):
            # if this roll failed ..
            if roll < success_threshold:
                roll += str_modifier  # Add current str_modifier to roll
                if roll > success_threshold:  # but if then roll exceeds success_threshold

                    # Put exceeded part back ..
                    str_modifier = roll - success_threshold
                    roll = success_threshold  # .. and set roll to exactly success_threshold
                else:
                    str_modifier = 0  # Apply the modifier only once
            adjusted_rolls.append(roll)
        adjusted_rolls = adjusted_rolls[::-1]
    elif str_modifier < 0:
        for roll in dice_rolls:
            # if this roll succeeded ..
            if roll >= success_threshold and str_modifier < 0:
                roll += str_modifier  # Add current str_modifier to roll
                if roll < success_threshold - 1:  # but if then roll is lower then success_threshold - 1
                    # Put exceeded part back ..
                    str_modifier = roll - success_threshold + 1
                    roll = success_threshold - 1  # .. and set roll to exactly success_threshold - 1
                else:
                    str_modifier = 0  # Apply the modifier only once
            adjusted_rolls.append(roll)
    else:
        adjusted_rolls = dice_rolls.copy()

    success_count = sum(
        1 for roll in adjusted_rolls if roll >= success_threshold)
    failure_count = len(dice_rolls) - success_count
    
    # Get changed amount
    modifier = []
    for i in range(0, len(adjusted_rolls)):
        modifier.append(adjusted_rolls[i] - dice_rolls[i])

    return modifier, adjusted_rolls