"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    if remaining < 0:
        return 0
    else:
        return remaining

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time remaining.

    Parameters:
        elapsed_preparation_time (int): The baking time already elapsed.

    Returns:
        int: The preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the actual minutes the lasagna has been prepared as
    an argument and returns how many minutes the lasagna still needs to be prepared
    based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return preparation_time_in_minutes(number_of_layers) + (EXPECTED_BAKE_TIME - bake_time_remaining(elapsed_bake_time))
