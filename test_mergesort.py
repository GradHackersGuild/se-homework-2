"""
Module implementing the unit test cases for Merge Sort algorithm.
"""
import hw2_debugging as OP


def test_mergesort1():
    """
    Takes array of random integers and checks whether it is sorted or not
    """
    arr = [10, 12, 2, 4, 1, 14, 10, 15, 16, 7, 9, 10]
    assert OP.merge_sort(arr) == [1, 2, 4, 7, 9, 10, 10, 10, 12, 14, 15, 16]


def test_mergesort2():
    """
    Takes array of random integers and checks whether it is sorted or not
    """
    arr = [8, 12, 2, 1, 4, 10, 14, 15, 20, 7, 9, 4]
    assert OP.merge_sort(arr) == [1, 2, 4, 4, 7, 8, 9, 10, 12, 14, 15, 20]


def test_mergesort3():
    """
    Takes array of random integers and checks whether it is sorted or not
    """
    arr = [-10, -17, -5, -5, -3, 1, -1000, 10]
    assert OP.merge_sort(arr) == [-1000, -17, -10, -5, -5, -3, 1, 10]
