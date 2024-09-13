"""
Module implementing the Merge Sort algorithm.

This script contains functions to perform merge sort on a given list and merge two sorted arrays.
"""
import rand

def merge_sort(arr):
    """
    Recursively divides and sorts an array using the merge sort algorithm.
    
    :param array: List of integers to be sorted.
    :return: Sorted list of integers.
    """
    if len(arr) == 1:
        return arr
    half = len(arr)//2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.
    
    :param left_arr: Left half sorted array.
    :param right_arr: Right half sorted array.
    :return: Merged sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]
    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]
    return merge_arr

array = rand.random_array([int] * 20)
arr_out = merge_sort(array)

print(arr_out)
