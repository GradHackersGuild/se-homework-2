"""
Module for generating random arrays.

This module contains a function to create a list of random integers.
"""

import random


def random_array(arr) -> list[int]:
    """
    Fill the provided list with random integers between 1 and 20.

    :param arr: List of integers to be filled with random values.
    :return: The list filled with random integers.
    """
    for i, _ in enumerate(arr):
        arr[i] = random.randint(1, 20)
    return arr
