"""
Module providing NUMERICAL functions to make attack rolls.
"""

import random
import src.roll_modifier as rmod

def roll_dice(num_dice):
    """
    Roll a specified number of six-sided dice and return the results sorted in descending order.

    Args:
        num_dice (int): Number of dice to roll.

    Returns:
        list: A list of dice results sorted in descending order.
    """
    dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return sorted(dice_rolls, reverse=False)


def calculate_success_and_failure(dice_rolls, str_modifier, success_threshold=4):
    """
    This function is moved to roll_modifier.py, and I left a link here.
    
    Calculate the number of success and failure dice based on the dice rolls and strength modifier.

    Args:
        dice_rolls (list): List of dice results. Dice must be increasing order!
        str_modifier (int): Strength modifier to adjust the dice results.

    Returns:
        tuple: A tuple containing the number of success dice, failure dice, and adjusted dice results.
    """

    # DICE ROLLS MUST BE IN INCREASING ORDER!
    # Apply positive or negative modifier starting from the highest failure die
    
    # See roll_modifier.py
    _, adjusted_rolls, success_count, failure_count =\
        rmod.modify(dice_rolls, str_modifier, success_threshold)

    return success_count, failure_count, adjusted_rolls


def check_hit(failure_count, enemy_evasion):
    """
    Determine if the attack hits based on the number of failure dice and the enemy's evasion value.

    Args:
        failure_count (int): Number of failure dice.
        enemy_evasion (int): Enemy's evasion value.

    Returns:
        bool: True if the attack hits, False if it misses.
    """
    return failure_count <= enemy_evasion


def calculate_damage(success_count, weapon_multiplier):
    """
    Calculate the damage dealt based on the number of success dice and the weapon's damage multiplier.

    Args:
        success_count (int): Number of success dice.
        weapon_multiplier (int): Weapon's damage multiplier.

    Returns:
        int: The total damage dealt.
    """
    return success_count * weapon_multiplier


def simulate_attack(num_dice, str_modifier, enemy_evasion, weapon_multiplier, do_print=False):
    """
    Simulate an attack by rolling dice, adjusting for strength, checking hit, and calculating damage.

    Args:
        num_dice (int): Number of dice to roll for the attack.
        str_modifier (int): Strength modifier to adjust the dice results.
        enemy_evasion (int): Enemy's evasion value to determine if the attack hits.
        weapon_multiplier (int): Weapon's damage multiplier for calculating damage.

    Returns:
        None
    """
    # Roll the dice
    dice_rolls = roll_dice(num_dice)

    # Calculate success and failure counts after adjusting for strength modifier
    success_count, failure_count, adjusted_rolls = calculate_success_and_failure(
        dice_rolls, str_modifier)

    # Check if the attack hits
    if check_hit(failure_count, enemy_evasion):
        # Calculate and print damage if the attack hits
        damage = calculate_damage(success_count, weapon_multiplier)
        # print(f"Attack hits! Damage dealt: {damage}")
    else:
        damage = 0
        failure_count = failure_count + success_count
        success_count = 0
    if do_print:
        print(f"Original dice rolls: {dice_rolls}")
        print(f"Adjusted dice rolls: {adjusted_rolls}")
        print(f"Success count: {success_count}, Failure count: {failure_count}")
    return dice_rolls, adjusted_rolls, success_count, failure_count, damage

